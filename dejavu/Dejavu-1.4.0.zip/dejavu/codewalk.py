"""Bytecode visitors, including rewriters and decompilers.

This work, including the source code, documentation
and related data, is placed into the public domain.

The orginal author is Robert Brewer, Amor Ministries.

THIS SOFTWARE IS PROVIDED AS-IS, WITHOUT WARRANTY
OF ANY KIND, NOT EVEN THE IMPLIED WARRANTY OF
MERCHANTABILITY. THE AUTHOR OF THIS SOFTWARE
ASSUMES _NO_ RESPONSIBILITY FOR ANY CONSEQUENCE
RESULTING FROM THE USE, MODIFICATION, OR
REDISTRIBUTION OF THIS SOFTWARE.

"""

from opcode import cmp_op, opname, opmap, HAVE_ARGUMENT
import operator
import sets
from types import CodeType, FunctionType


def named_opcodes(bits):
    """Change initial numeric opcode bits to their named equivalents."""
    bitnums = []
    bits = iter(bits)
    for x in bits:
        bitnums.append(opname[x])
        if x >= HAVE_ARGUMENT:
            try:
                bitnums.append(bits.next())
                bitnums.append(bits.next())
            except StopIteration:
                break
    return bitnums

def numeric_opcodes(bits):
    """Change named opcode bits to their numeric equivalents."""
    bitnums = []
    for x in bits:
        if isinstance(x, basestring):
            x = opmap[x]
        bitnums.append(x)
    return bitnums

_deref_bytecode = numeric_opcodes(['LOAD_DEREF', 0, 0, 'RETURN_VALUE'])
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants,
#          names, varnames, filename, name, firstlineno,
#          lnotab[, freevars[, cellvars]])
_derefblock = CodeType(0, 0, 1, 3, ''.join(map(chr, _deref_bytecode)),
                       (None,), ('cell',), (), '', '', 2, '', ('cell',))
def deref_cell(cell):
    # FunctionType(code, globals[, name[, argdefs[, closure]]])
    return FunctionType(_derefblock, {}, "", (), (cell,))()

def make_closure(*args):
    def inner():
        args
    return inner.func_closure


binary_operators = {'BINARY_POWER': operator.pow,
                    'BINARY_MULTIPLY': operator.mul,
                    'BINARY_DIVIDE': operator.div,
                    'BINARY_FLOOR_DIVIDE': operator.floordiv,
                    'BINARY_TRUE_DIVIDE': operator.truediv,
                    'BINARY_MODULO': operator.mod,
                    'BINARY_ADD': operator.add,
                    'BINARY_SUBTRACT': operator.sub,
                    'BINARY_SUBSCR': operator.getitem,
                    'BINARY_LSHIFT': operator.lshift,
                    'BINARY_RSHIFT': operator.rshift,
                    'BINARY_AND': operator.and_,
                    'BINARY_XOR': operator.xor,
                    'BINARY_OR': operator.or_,
                    }
inplace_operators = dict([('INPLACE_' + k.split('_')[1], v)
                          for k, v in binary_operators.iteritems()
                          if k not in ('BINARY_SUBSCR',)
                          ])

binary_repr = {'BINARY_POWER': '**',
               'BINARY_MULTIPLY': '*',
               'BINARY_DIVIDE': '/',
               'BINARY_FLOOR_DIVIDE': '//',
               'BINARY_TRUE_DIVIDE': '/',
               'BINARY_MODULO': '%',
               'BINARY_ADD': '+',
               'BINARY_SUBTRACT': '-',
               'BINARY_LSHIFT': '<<',
               'BINARY_RSHIFT': '>>',
               'BINARY_AND': '&',
               'BINARY_XOR': '^',
               'BINARY_OR': '|',
               }

inplace_repr = dict([('INPLACE_' + k.split('_')[1], v + '=')
                     for k, v in binary_repr.iteritems()])

comparisons = {'<': operator.lt,
               '<=': operator.le,
               '==': operator.eq,
               '!=': operator.ne,
               '>': operator.gt,
               '>=': operator.gt,
               'in': operator.contains,
               'not in': lambda x, y: not x in y,
               'is': operator.is_,
               'is not': operator.is_not,
               }

_co_code_attrs = ['co_argcount', 'co_cellvars', 'co_code', 'co_consts',
                  'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars',
                  'co_lnotab', 'co_name', 'co_names', 'co_nlocals',
                  'co_stacksize', 'co_varnames']


class Visitor(object):
    """Visitor(obj=function, code object, string, or list of opcodes)."""
    
    def __init__(self, obj):
        self.verbose = False
        
        # Distill supplied 'obj' arg to a code block string.
        if isinstance(obj, FunctionType):
            obj = obj.func_code
        try:
            obj = obj.co_code
        except AttributeError:
            pass
        
        # Map the code block string to a list of opcode numbers.
        if isinstance(obj, basestring):
            obj = map(ord, obj)
        elif isinstance(obj, list):
            obj = obj[:]
        
        self._bytecode = obj
    
    def debug(self, *messages):
        if self.verbose:
            for term in messages:
                print term,
        else:
            pass
    
    def walk(self):
        self.cursor = 0
        b = self._bytecode
        self.debug("\nWALKING: ", b)
        while self.cursor < len(b):
            self.debug("\n", self.cursor)
            
            op = b[self.cursor]
            self.cursor += 1
            if op >= HAVE_ARGUMENT:
                lo = b[self.cursor]
                self.cursor += 1
                hi = b[self.cursor]
                self.cursor += 1
                args = (lo, hi)
            else:
                args = ()
            
            self.debug("visit (%s, %s)" % (op, repr(args)))
            self.visit_instruction(op, *args)
            
            name = 'visit_' + opname[op]
            name = name.replace('+', '_PLUS_')
            handler = getattr(self, name, None)
            if handler:
                self.debug("=> %s%s" % (name[6:], repr(args)))
                handler(*args)
    
    def visit_instruction(self, op, lo=None, hi=None):
        pass


class JumpCodeAdjuster(Visitor):
    """JumpCodeAdjuster(obj=[func|co|str|list], start, end, newlength).
    
    Adjusts jump codes if their target is affected by bytecode changes.
    
    start, end: The range of the original bytecode in question.
    newlength: Length of the codes which overwrote bytecode[start:end].
    """
    
    def __init__(self, obj, start, end, newlength):
        Visitor.__init__(self, obj)
        self.start = start
        self.end = end
        self.offset = newlength - (end - start)
    
    def bytecode(self):
        """Walk self and return new bytecode."""
        self.walk()
        return self.newcode
    
    def walk(self):
        if self.offset == 0:
            # Avoid costly walk if no changes will be made.
            self.newcode = self._bytecode
        else:
            self.newcode = []
            Visitor.walk(self)
    
    def visit_instruction(self, op, lo=None, hi=None):
        append = self.newcode.append
        append(op)
        if lo is not None:
            append(lo)
        if hi is not None:
            append(hi)
    
    def visit_CONTINUE_LOOP(self, lo, hi):
        self.visit_JUMP_ABSOLUTE(lo, hi)
    
    def visit_JUMP_ABSOLUTE(self, lo, hi):
        target = lo + (hi << 8)
        if target > self.start:
            pos = target + self.offset
            self.newcode[-2:] = [pos & 0xFF, pos >> 8]
    
    def visit_JUMP_FORWARD(self, lo, hi):
        delta = lo + (hi << 8)
        target = self.cursor + delta
        if self.cursor < self.end and target > self.start:
            pos = (target + self.offset) - self.cursor
            self.newcode[-2:] = [pos & 0xFF, pos >> 8]
    
    def visit_JUMP_IF_FALSE(self, lo, hi):
        self.visit_JUMP_FORWARD(lo, hi)
    
    def visit_JUMP_IF_TRUE(self, lo, hi):
        self.visit_JUMP_FORWARD(lo, hi)


def safe_tuple(seq):
    """Force func_code attributes to tuples of strings.
    
    Many of the func_code attributes must take tuples, not lists,
    and *cannot* accept unicode items--they must be coerced to strings
    or the interpreter will crash.
    """
    seq = map(str, seq)
    return tuple(seq)


class Rewriter(Visitor):
    """Rewriter(obj=function or code object).
    
    Produce a new function or code object by rewriting an existing one.
    
    Notice that, unlike the base Visitor class, Rewriter does not accept a
    string or list of opcodes as an initial argument.
    """
    
    def __init__(self, obj):
        self.verbose = False
        
        if isinstance(obj, FunctionType):
            self._func = obj
            obj = obj.func_code
        
        # Copy code object attributes.
        for name in _co_code_attrs:
            value = getattr(obj, name)
            if isinstance(value, tuple):
                value = list(value)
            setattr(self, name, value)
        
        try:
            obj = obj.co_code
        except AttributeError:
            pass
        
        # Map the code block to a list of opcode numbers.
        if isinstance(obj, basestring):
            bytecode = map(ord, obj)
        elif isinstance(obj, list):
            bytecode = obj[:]
        else:
            raise TypeError("obj arg of incorrect type '%s'" % type(obj))
        
        self._bytecode = bytecode
    
    def bytecode(self):
        """Walk self and return new bytecode."""
        self.walk()
        return self.newcode
    
    def code_object(self):
        """Walk self and produce a new code object."""
        self.walk()
        codestr = ''.join(map(chr, self.newcode))
        return CodeType(self.co_argcount, self.co_nlocals, self.co_stacksize,
                        # Notice co_consts should *not* be safe_tupled.
                        self.co_flags, codestr, tuple(self.co_consts),
                        safe_tuple(self.co_names), safe_tuple(self.co_varnames),
                        self.co_filename, self.co_name, self.co_firstlineno,
                        self.co_lnotab, safe_tuple(self.co_freevars),
                        safe_tuple(self.co_cellvars))
    
    def function(self, newname=None):
        """Walk self and produce a new function."""
        try:
            f = self._func
        except AttributeError:
            if newname is None:
                newname = ''
            co = self.code_object()
            return FunctionType(co, {}, newname)
        else:
            if newname is None:
                newname = f.func_name
            co = self.code_object()
            return FunctionType(co, f.func_globals, newname,
                                f.func_defaults, f.func_closure)
    
    def const_index(self, value):
        """The index of value in co_consts, appending it if not found."""
        for pos, item in enumerate(self.co_consts):
            try:
                if type(value) == type(item) and value == item:
                    break
            except TypeError:
                pass
        else:
            pos = len(self.co_consts)
            self.co_consts.append(value)
        return pos
    
    def name_index(self, value):
        """The index of value in co_names, appending it if not found."""
        valtype = type(value)
        for pos, item in enumerate(self.co_names):
            try:
                if valtype == type(item) and value == item:
                    return pos
            except TypeError:
                pass
        
        pos = len(self.co_names)
        self.co_names.append(value)
        return pos
    
    def walk(self):
        self.newcode = []
        Visitor.walk(self)
    
    def visit_instruction(self, op, lo=None, hi=None):
        append = self.newcode.append
        append(op)
        if lo is not None:
            append(lo)
        if hi is not None:
            append(hi)
    
    def put(self, start, end, *bits):
        """Overwrite self.newcode with new opcodes (numbers or names).
        
        If the new codes are of different quantity than the old,
        modify any jump codes affected.
        """
        bitnums = numeric_opcodes(bits)
        
        # Adjust jump codes. Notice this comes before bytecode is modified.
        jca = JumpCodeAdjuster(self.newcode, start, end, len(bitnums))
        self.newcode = jca.bytecode()
        
        # Rewrite bytecode.
        self.newcode[start:end] = bitnums
    
    def tail(self, length, *bits):
        """Overwrite self.newcode[-length:] with bits."""
        end = len(self.newcode)
        self.put(end - length, end, *bits)


class Localizer(Rewriter):
    """Localizer(func, builtin_only=False, stoplist=[], verbose=False)
    
    If a global or builtin is known at compile time, replace it with a constant.
    
    This duplicates (and borrows from) Raymond Hettinger's Cookbook recipe
    at: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/277940
    """
    def __init__(self, func, builtin_only=False, stoplist=[], verbose=False):
        Rewriter.__init__(self, func)
        
        import __builtin__
        self.env = vars(__builtin__).copy()
        if not builtin_only:
            self.env.update(func.func_globals)
        
        self.stoplist = stoplist
        self.verbose = verbose
    
    def visit_LOAD_GLOBAL(self, lo, hi):
        name = self.co_names[lo + (hi << 8)]
        if name in self.env and name not in self.stoplist:
            value = self.env[name]
            pos = self.const_index(value)
            self.tail(3, 'LOAD_CONST', pos & 0xFF, pos >> 8)
            self.debug(name, ' --> ', value)


class TaintableStack(list):
    def __init__(self, seq=[]):
        list.__init__(self, seq)
        self._taintindex = sets.Set()
        self.maxsize = len(seq)
    
    def taint(self, index=-1):
        if index < 0:
            index += len(self)
        self._taintindex.add(index)
    
    def tainted(self, index=-1):
        if index < 0:
            index = len(self) + index
        return (index in self._taintindex)
    
    def pop(self, index=-1):
        """pop(index) -> Returns a tuple!! of (value, tainted)."""
        if index < 0:
            index += len(self)
        is_tainted = (index in self._taintindex)
        if is_tainted:
            self._taintindex.remove(index)
        return list.pop(self, index), is_tainted
    
    def append(self, obj):
        list.append(self, obj)
        l = len(self)
        if l > self.maxsize:
            self.maxsize = l


class EarlyBinder(Rewriter):
    """EarlyBinder(func, reduce_getattr=True, bind_late=[])
    
    Deep-evaluate function, replacing free vars with constants.
    
    reduce_getattr: If True (the default), getattr(x, y) will be
        replaced with x.y where possible.
    
    bind_late: a list of names (globals, freevars, or attributes)
        which should not be early-bound. For example, if you want
        datetime.date.today() to be bound late, include 'today'
        in the bind_late.
    
    Example: k = lambda x: x.Date == datetime.date(2004, 1, 1)
             r = EarlyBinder(k).function()
             
    _____ k _____                _____ r _____
     0 LOAD_FAST     0 (x)        0 LOAD_FAST   0 (x)
     3 LOAD_ATTR     1 (Date)     3 LOAD_ATTR   1 (Date)
     6 LOAD_GLOBAL   2 (datetime) 6 LOAD_CONST  6 (datetime.date(2004, 1, 1))
     9 LOAD_ATTR     3 (date)
    12 LOAD_CONST    1 (2004)
    15 LOAD_CONST    2 (1)
    18 LOAD_CONST    2 (1)
    21 CALL_FUNCTION 3
    24 COMPARE_OP    2 (==)       9 COMPARE_OP  2 (==)
    27 RETURN_VALUE              12 RETURN_VALUE
    
    This also pre-computes binary operations *and all other builtin or free
    functions* where all operands are constants, globals, or freevars.
    For example:
        LOAD_CONST        1 (3)
        LOAD_CONST        2 (4)
        BINARY_MULTIPLY
        
    is replaced with:
        LOAD_CONST        5 (12)
    
    However, order is important. lambda x: x * 4 * 5 won't see any
    optimization, because the order of eval is (x * 4) * 5. Rewritten
    as lambda x: 4 * 5 * x, the "4 * 5" can be replaced with "20".
    """
    
    def __init__(self, func, reduce_getattr=True, bind_late=[]):
        Rewriter.__init__(self, func)
        self.reduce_getattr = reduce_getattr
        
        import __builtin__
        self.env = vars(__builtin__).copy()
        self.env.update(func.func_globals)
        
        # Keep a stack like the interpreter would. This does *not*
        # get overwritten when self.newcode does--it emulates the
        # original instructions (although tainted values may be dummies).
        # When a local var is pushed onto this stack, it "taints" itself
        # and any operations which depend upon it.
        # This stack is not passed out of this class in any way.
        self.stack = TaintableStack()
        self.bind_late = bind_late
    
    def code_object(self):
        """Walk self and produce a new code object."""
        self.walk()
        codestr = ''.join(map(chr, self.newcode))
        # Assert CO_NOFREE, since all free vars should have been made constant.
        self.co_flags |= 0x0040
        co = CodeType(self.co_argcount, self.co_nlocals, self.stack.maxsize,
                      self.co_flags, codestr, tuple(self.co_consts),
                      safe_tuple(self.co_names), safe_tuple(self.co_varnames),
                      '', self.co_name, 1,
                      self.co_lnotab, (), ())
        return co
    
    def function(self, newname=None):
        """Walk self and produce a new function."""
        try:
            f = self._func
        except AttributeError:
            if newname is None:
                newname = ''
            co = self.code_object()
            return FunctionType(co, {}, newname)
        else:
            if newname is None:
                newname = f.func_name
            co = self.code_object()
            # All cells should be dereferenced, so force func_closure to None.
            return FunctionType(co, f.func_globals, newname, f.func_defaults)
    
    def reduce(self, number_of_terms, transform=None, overwrite_length=None):
        """If no stack args are to be bound late, rewrite previous opcodes.
        
        number_of_terms: the number of terms to pop off the stack.
        
        transform: a callback, to which we send the popped terms. They are
            transformed in that function as needed, and returned.
        
        overwrite_length: the number of previous opcodes to overwrite. If
            None, it defaults to (number of terms + 1 for the current
            instruction) * 3.
        """
        if overwrite_length is None:
            # +1 is for current bytecode. If any overwritten bytecode
            # is not len 3, pass in a value for overwrite_length.
            overwrite_length = (number_of_terms + 1) * 3
        
        # Pop the requested number of terms off the stack.
        is_tainted = False
        terms, taints = [], []
        for i in xrange(number_of_terms):
            term, taint = self.stack.pop()
            taints.append(taint)
            is_tainted |= taint
            terms.append(term)
        
        # Now that all the stack-popping is done...
        if is_tainted:
            # We don't have to handle getattr if no args are
            # tainted, because CALL_FUNCTION will do it normally.
            if self.reduce_getattr:
                if (len(terms) == 3 and terms[2] == getattr
                    and taints[1] and not taints[0]):
                    # Form a new LOAD_ATTR instruction.
                    pos = self.name_index(terms[0])
                    # Unlike normal CALL_FUNCTION, we can't assume each arg
                    # is a constant; therefore, our overwrite_length is
                    # indeterminate. We'll just cheat and keep track of
                    # the last LOAD_GLOBAL where we looked up getattr. ;)
                    start = self.last_getattr
                    # Grab and reuse opcodes of first (LOAD_FAST) term.
                    bits = self.newcode[start + 3:-6]
                    bits += ['LOAD_ATTR', pos & 0xFF, pos >> 8]
                    bits = tuple(bits)
                    self.put(start, len(self.newcode), *bits)
                    self.stack.append(None)
                    self.stack.taint()
                    return None
            
            # Don't form the new object.
            # Replace TOS with a dummy and taint it.
            self.stack.append(None)
            self.stack.taint()
            return None
        
        # Callback the transform.
        terms.reverse()
        if transform:
            result = transform(terms)
        else:
            result = terms
        
        # Replace TOS with result.
        self.stack.append(result)
        
        # Overwrite bytecodes with new CONST formed from result.
        pos = self.const_index(result)
        self.tail(overwrite_length, 'LOAD_CONST', pos & 0xFF, pos >> 8)
        
        return result
    
    def visit_BUILD_TUPLE(self, lo, hi):
        self.reduce(lo + (hi << 8), lambda terms: tuple(terms))
    
    def visit_BUILD_LIST(self, lo, hi):
        self.reduce(lo + (hi << 8))
    
    def visit_CALL_FUNCTION(self, lo, hi):
        def call(terms):
            func = terms.pop(0)
            args = tuple(terms[:lo])
            kwargs = {}
            for i in range(hi):
                key = self.terms.pop(0)
                val = self.terms.pop(0)
                kwargs[key] = val
            return func(*args, **kwargs)
        self.reduce(lo + hi + 1, call)
    
    def visit_COMPARE_OP(self, lo, hi):
        op = cmp_op[lo + (hi << 8)]
        op = comparisons[op]
        self.reduce(2, lambda terms: op(*terms))
    
    def visit_LOAD_ATTR(self, lo, hi):
        name = self.co_names[lo + (hi << 8)]
        result = self.reduce(1, lambda terms: getattr(terms[0], name))
        if result in self.bind_late or getattr(result, 'bind_late', False):
            self.stack.taint()
    
    def visit_LOAD_CONST(self, lo, hi):
        self.stack.append(self.co_consts[lo + (hi << 8)])
    
    def visit_LOAD_DEREF(self, lo, hi):
        if hasattr(self, '_func'):
            name = self.co_freevars[lo + (hi << 8)]
            value = self._func.func_closure[lo + (hi << 8)]
            value = deref_cell(value)
            pos = self.const_index(value)
            self.tail(3, 'LOAD_CONST', pos & 0xFF, pos >> 8)
            self.stack.append(value)
            if value in self.bind_late or getattr(value, 'bind_late', False):
                self.stack.taint()
    
    def visit_LOAD_FAST(self, lo, hi):
        self.stack.append(self.co_varnames[lo + (hi << 8)])
        # LOAD_FAST references our bound variable, which is always bound late.
        self.stack.taint()
    
    def visit_LOAD_GLOBAL(self, lo, hi):
        name = self.co_names[lo + (hi << 8)]
        if name == 'getattr':
            self.last_getattr = (len(self.newcode) - 3)
        if name in self.env:
            value = self.env[name]
            pos = self.const_index(value)
            self.tail(3, 'LOAD_CONST', pos & 0xFF, pos >> 8)
            self.stack.append(value)
            if value in self.bind_late or getattr(value, 'bind_late', False):
                self.stack.taint()
        else:
            raise KeyError("'%s' is not present in supplied globals." % name)
    
    def visit_SLICE_PLUS_0(self):
        self.reduce(1, lambda terms: terms[0][:], 4)
    
    def visit_SLICE_PLUS_1(self):
        self.reduce(2, lambda terms: terms[0][terms[1]:], 7)
    
    def visit_SLICE_PLUS_2(self):
        self.reduce(2, lambda terms: terms[0][:terms[1]], 7)
    
    def visit_SLICE_PLUS_3(self):
        self.reduce(3, lambda terms: terms[0][terms[1]:terms[2]], 10)
    
    def binary_op(self, op):
        def operate(terms):
            return op(*terms)
        self.reduce(2, operate, 7)

# Add visit_BINARY, visit_INPLACE methods to EarlyBinder.
for k, v in binary_operators.iteritems():
    setattr(EarlyBinder, "visit_" + k,
            lambda self, opr=v: self.binary_op(opr))
for k, v in inplace_operators.iteritems():
    setattr(EarlyBinder, "visit_" + k,
            # Yes, we really do call binary_op for inplace methods.
            lambda self, opr=v: self.binary_op(opr))


class LambdaDecompiler(Visitor):
    """LambdaDecompiler(obj=lambda function or func_code).
    
    Produce decompiled Python code (as a string) from a supplied lambda."""
    
    def __init__(self, obj):
        self.verbose = False
        
        # Distill supplied 'obj' arg to a code block string.
        if isinstance(obj, FunctionType):
            obj = obj.func_code
        
        # Copy code object attributes.
        for name in _co_code_attrs:
            value = getattr(obj, name)
            if isinstance(value, tuple):
                value = list(value)
            setattr(self, name, value)
        
        try:
            obj = obj.co_code
        except AttributeError:
            pass
        
        # Map the code block to a list of opcode numbers.
        if isinstance(obj, basestring):
            obj = map(ord, obj)
        elif isinstance(obj, list):
            obj = obj[:]
        
        self._bytecode = obj
    
    def code(self, include_func_header=True):
        self.walk()
        product = self.stack[0]
        if include_func_header:
            args = list(self.co_varnames)
            if self.co_flags & 0x08:
                args[-1] = "**" + args[-1]
                if self.co_flags & 0x04:
                    args[-2] = "*" + args[-2]
            elif self.co_flags & 0x04:
                args[-1] = "*" + args[-1]
            args = ", ".join(args)
            
            product = "lambda %s: %s" % (args, product)
        return product
    
    def walk(self):
        self.stack = []
        self.newcode = []
        self.targets = {}
        
        Visitor.walk(self)
        
        self.debug("stack:", self.stack)
    
    def visit_instruction(self, op, lo=None, hi=None):
        # Get the instruction pointer for the current instruction.
        ip = self.cursor - 3
        if hi is None:
            ip += 1
            if lo is None:
                ip += 1
        
        terms = self.targets.get(ip)
        if terms:
            clause = self.stack[-1]
            while terms:
                term, oper = terms.pop()
                clause = "(%s) %s (%s)" % (term, oper, clause)
            # Replace TOS with the new clause, so that further
            # combinations have access to it.
            self.stack[-1] = clause
            self.debug("clause:", clause, "\n")
            
            if op == 1:
                # Py2.4: The current instruction is POP_TOP, which means
                # the previous is probably JUMP_*. If so, we don't want to
                # pop the value we just placed on the stack and lose it.
                # We need to replace the entry that the JUMP_* made in
                # self.targets with our new TOS.
                target = self.targets[self.last_target_ip]
                target[-1] = ((clause, target[-1][1]))
                self.debug("newtarget:", self.last_target_ip, target)
    
    def visit_BUILD_TUPLE(self, lo, hi):
        terms = ", ".join([self.stack.pop() for i in range(lo + hi << 8)])
        self.stack.append("(%s)" % terms)
    
    def visit_BUILD_LIST(self, lo, hi):
        terms = ", ".join([self.stack.pop() for i in range(lo + hi << 8)])
        self.stack.append("[%s]" % terms)
    
    def visit_CALL_FUNCTION(self, lo, hi):
        kwargs = {}
        for i in range(hi):
            val = self.stack.pop()
            key = self.stack.pop()
            kwargs[key] = val
        kwargs = ", ".join([k + "=" + v for k, v in kwargs.iteritems()])
        
        args = []
        for i in xrange(lo):
            arg = self.stack.pop()
            args.append(arg)
        args.reverse()
        args = ", ".join(args)
        
        if kwargs:
            args += ", " + kwargs
        
        func = self.stack.pop()
        self.stack.append("%s(%s)" % (func, args))
    
    def visit_COMPARE_OP(self, lo, hi):
        term2, term1 = self.stack.pop(), self.stack.pop()
        op = cmp_op[lo + (hi << 8)]
        self.stack.append(term1 + " " + op + " " + term2)
        self.debug(op)
    
    def visit_JUMP_IF_FALSE(self, lo, hi):
        # Note that self.cursor has already advanced to the next instruction.
        target = self.cursor + (lo + (hi << 8))
        bucket = self.targets.setdefault(target, [])
        bucket.append((self.stack[-1], 'and'))
        self.debug("target:", target, bucket)
        # Store target ip for the special code in visit_instruction
        self.last_target_ip = target
    
    def visit_JUMP_IF_TRUE(self, lo, hi):
        # Note that self.cursor has already advanced to the next instruction.
        target = self.cursor + (lo + (hi << 8))
        bucket = self.targets.setdefault(target, [])
        bucket.append((self.stack[-1], 'or'))
        self.debug("target:", target, bucket)
        # Store target ip for the special code in visit_instruction
        self.last_target_ip = target
    
    def visit_LOAD_ATTR(self, lo, hi):
        term = self.co_names[lo + (hi << 8)]
        self.stack[-1] += ("." + term)
        self.debug(term)
    
    def visit_LOAD_CONST(self, lo, hi):
        val = self.co_consts[lo + (hi << 8)]
        if isinstance(val, (FunctionType, type)):
            # The const in question is a factory function.
            self.stack.append(val.__module__ + "." + val.__name__)
        else:
            term = repr(val)
            if hasattr(val, "__module__"):
                if not term.startswith(val.__module__ + "."):
                    term = val.__module__ + "." + term
            self.stack.append(term)
            self.debug(term)
    
    def visit_LOAD_FAST(self, lo, hi):
        term = self.co_varnames[lo + (hi << 8)]
        self.stack.append(term)
        self.debug(term)
    
    def visit_LOAD_GLOBAL(self, lo, hi):
        self.stack.append(self.co_names[lo + (hi << 8)])
    
    def visit_POP_TOP(self):
        self.stack.pop()
    
    def visit_SLICE_PLUS_0(self):
        arg = self.stack.pop()
        self.stack.append("%s[:]" % arg)
    
    def visit_SLICE_PLUS_1(self):
        args = tuple(self.stack[-2:])
        del self.stack[-2:]
        self.stack.append("%s[%s:]" % args)
    
    def visit_SLICE_PLUS_2(self):
        args = tuple(self.stack[-2:])
        del self.stack[-2:]
        self.stack.append("%s[:%s]" % args)
    
    def visit_SLICE_PLUS_3(self):
        args = tuple(self.stack[-3:])
        del self.stack[-3:]
        self.stack.append("%s[%s:%s]" % args)
    
    def visit_UNARY_CONVERT(self):
        term = self.stack.pop()
        self.stack.append("`(" + term + ")`")
    
    def visit_UNARY_INVERT(self):
        term = self.stack.pop()
        self.stack.append("~(" + term + ")")
    
    def visit_UNARY_NEGATIVE(self):
        term = self.stack.pop()
        self.stack.append("-(" + term + ")")
    
    def visit_UNARY_NOT(self):
        term = self.stack.pop()
        self.stack.append("not (" + term + ")")
    
    def visit_UNARY_POSITIVE(self):
        term = self.stack.pop()
        self.stack.append("+(" + term + ")")
    
    def binary_op(self, op):
        op2, op1 = self.stack.pop(), self.stack.pop()
        self.stack.append(op1 + " " + op + " " + op2)
    
    def visit_BINARY_SUBSCR(self):
        op2, op1 = self.stack.pop(), self.stack.pop()
        self.stack.append(op1 + "[" + op2 + "]")

# Add visit_BINARY methods to LambdaDecompiler.
for k, v in binary_repr.iteritems():
    setattr(LambdaDecompiler, "visit_" + k,
            lambda self, op=v: self.binary_op(op))


class BranchTracker(Visitor):
    """BranchTracker(obj=[func|co|str|list]).
    
    Finds all possible instructions previous to the supplied instruction(s).
    """
    
    def branches(self, instr=None):
        """Walk self and return all possible instructions previous to instr.
        
        If instr is None, the last instruction will be used.
        """
        if instr is None:
            instr = len(self._bytecode) - 1
        self.watch = {instr: []}
        self.walk()
        return self.watch[instr]
    
    def visit_instruction(self, op, lo=None, hi=None):
        if self.cursor in self.watch and op != 113:
            if lo is None and hi is None:
                self.watch[self.cursor].append(self.cursor - 1)
            else:
                self.watch[self.cursor].append(self.cursor - 3)
    
    def visit_CONTINUE_LOOP(self, lo, hi):
        self.visit_JUMP_ABSOLUTE(lo, hi)
    
    def visit_JUMP_ABSOLUTE(self, lo, hi):
        target = lo + (hi << 8)
        if target in self.watch:
            self.watch[target].append(self.cursor)
    
    def visit_JUMP_FORWARD(self, lo, hi):
        delta = lo + (hi << 8)
        target = self.cursor + delta
        if target in self.watch:
            self.watch[target].append(self.cursor - 3)
    
    def visit_JUMP_IF_FALSE(self, lo, hi):
        self.visit_JUMP_FORWARD(lo, hi)
    
    def visit_JUMP_IF_TRUE(self, lo, hi):
        self.visit_JUMP_FORWARD(lo, hi)


class KeywordInspector(Rewriter):
    """Produce a list of all keyword arguments expected."""
    
    def __init__(self, obj):
        """KeywordInspector(obj). List keyword arguments expected."""
        Rewriter.__init__(self, obj)
        if not (self.co_flags & 0x0008):
            raise ValueError("'%s' does not possess **kwargs." % obj)
        if len(self.co_varnames) <= 1:
            raise ValueError("'%s' does not possess more than 1 varname." % obj)
        self._kwargs = []
        self.flag = None
    
    def kwargs(self):
        """kwargs() -> List of keyword arguments expected."""
        self.walk()
        return self._kwargs
    
    def visit_instruction(self, op, lo=None, hi=None):
        if op == 124 and (lo + (hi << 8) == len(self.co_varnames) - 1):
            self.flag = ''
        elif op == 100 and self.flag == '':
            self.flag = self.co_consts[lo + (hi << 8)]
        elif op == 25 and self.flag:
            self._kwargs.append(self.flag)
        else:
            self.flag = None

del k, v

