# $Id$

# --------------------------------------------------------------------

__all__ = ['flaglist',
           'command',
           'makefile']

# --------------------------------------------------------------------

def append(seq, item):
    if item not in seq:
        seq.append(item)

def append_dict(conf, dct):
    for key, values in dct.iteritems():
        if key in conf:
            for value in values:
                if value not in conf[key]:
                    conf[key].append(value)

def flaglist(flags):

    conf = {
        'define_macros'       : [],
        'undef_macros'        : [],
        'include_dirs'        : [],
        
        'libraries'           : [],
        'library_dirs'        : [],
        'runtime_library_dirs': [],
        
        'extra_compile_args'  : [],
        'extra_link_args'     : [],
        }
    
    if type(flags) is str:
        flags = flags.split()
        
    switch = '-Wl,'
    newflags = []
    linkopts = []
    for f in flags:
        if f.startswith(switch):
            if len(f) > 4:
                append(linkopts, f[4:])
        else:
            append(newflags, f)
    if linkopts:
        newflags.append(switch + ','.join(linkopts))
    flags = newflags
        
    append_next_word = None

    for word in flags:

        if append_next_word is not None:
            append(append_next_word, word)
            append_next_word = None
            continue
       
        switch, value = word[0:2], word[2:]

        if switch == "-I":
            append(conf['include_dirs'], value)
        elif switch == "-D":
            try:
                idx = value.index("=")
                macro = (value[:idx], value[idx+1:])
            except ValueError:
                macro = (value, None)
            append(conf['define_macros'], macro)
        elif switch == "-U":
            append(conf['undef_macros'], value)
        elif switch == "-l":
            append(conf['libraries'], value)
        elif switch == "-L":
            append(conf['library_dirs'], value)
        elif switch == "-R":
            append(conf['runtime_library_dirs'], value)
        elif word.startswith("-Wl"):
            linkopts = word.split(',')
            append_dict(conf, flaglist(linkopts[1:]))
        elif word == "-rpath":
            append_next_word = conf['runtime_library_dirs']
        elif word == "-Xlinker":
            append_next_word = conf['extra_link_args']
        else:
            #log.warn("unrecognized flag '%s'" % word)
            pass
    return conf

# --------------------------------------------------------------------

from subprocess import Popen, PIPE, STDOUT

def command(cmd):
    """
    Return command 'stdout' and 'stderr' output (None if error)
    """
    if isinstance(cmd, str):
        args = cmd.split()
    else:
        args = list(cmd)
    try:
        child = Popen(args, stdout=PIPE, stderr=STDOUT)
        if child.wait():
            return None
        else:
            return child.stdout.read()
    except Exception:
        return None

# --------------------------------------------------------------------

from distutils.text_file import TextFile

# Regexes needed for parsing Makefile-like syntaxes
import re as sre
_variable_rx = sre.compile("([a-zA-Z][a-zA-Z0-9_]+)\s*=\s*(.*)")
_findvar1_rx = sre.compile(r"\$\(([A-Za-z][A-Za-z0-9_]*)\)")
_findvar2_rx = sre.compile(r"\${([A-Za-z][A-Za-z0-9_]*)}")

def makefile(fileobj, dct=None):
    """Parse a Makefile-style file.

    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    fp = TextFile(file=fileobj,
                  strip_comments=1,
                  skip_blanks=1,
                  join_lines=1)

    if dct is None:
        dct = {}
    done = {}
    notdone = {}

    while 1:
        line = fp.readline()
        if line is None:                # eof
            break
        m = _variable_rx.match(line)
        if m:
            n, v = m.group(1, 2)
            v = str.strip(v)
            if "$" in v:
                notdone[n] = v
            else:
                try: v = int(v)
                except ValueError: pass
                done[n] = v

    # do variable interpolation here
    while notdone:
        for name in notdone.keys():
            value = notdone[name]
            m = _findvar1_rx.search(value) or _findvar2_rx.search(value)
            if m:
                n = m.group(1)
                if done.has_key(n):
                    after = value[m.end():]
                    value = value[:m.start()] + str(done[n]) + after
                    if "$" in after:
                        notdone[name] = value
                    else:
                        try: value = int(value)
                        except ValueError:
                            done[name] = str.strip(value)
                        else:
                            done[name] = value
                        del notdone[name]
                elif notdone.has_key(n):
                    # get it on a subsequent round
                    pass
                else:
                    done[n] = ""
                    after = value[m.end():]
                    value = value[:m.start()] + after
                    if "$" in after:
                        notdone[name] = value
                    else:
                        try: value = int(value)
                        except ValueError:
                            done[name] = str.strip(value)
                        else:
                            done[name] = value
                        del notdone[name]
            else:
                # bogus variable reference; just drop it since we can't deal
                del notdone[name]

    fp.close()

    # save the results in the global dictionary
    dct.update(done)
    return dct

# --------------------------------------------------------------------
