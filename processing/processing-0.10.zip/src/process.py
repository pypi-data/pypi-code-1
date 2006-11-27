#
# Module providing the Process class which emulates threading.Thread
#
# processing/process.py
#
# Copyright (c) 2006, Richard Oudkerk
#

__all__ = [ 'Process', 'currentProcess' ]

import os, sys

class DummyProcess(object):

    def __init__(self):
        self._identity = ()
        self._name = 'MainProcess'

    def getName(self):
        return self._name

    def __repr__(self):
        if self._identity == ():
            return '<%s(MainProcess, started)>' % Process.__name__
        else:
            return '<%s(%s, started)>' % (type(self).__name__, self.getName())


class Process(DummyProcess):    
    '''
    Analogue of threading.Thread

    Differences:

    * join() does not have a timeout argument
    * setName() will not work after the process is started
    * isAlive() and setDaemon() are not implemented
    '''
    _this_process = DummyProcess()
    _counter = 0                              # should use mutex

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        self._group = group
        self._target = target
        self._args = args
        self._kwargs = kwargs

        self._state = 'initial'
        Process._counter += 1
        self._identity = Process._this_process._identity + (Process._counter,)

        if name is None:
            self._name = 'Process-' + ':'.join(map(str, self._identity))
        else:
            self._name = name

    def join(self):
        assert self._state == 'started'
        assert self is not currentProcess()
        res = os.waitpid(self._pid, 0)
        self._state = 'stopped'
        return res
    
    def run(self):        
        if self._target:
            self._target(*self._args, **self._kwargs)

    def _run(self):
        self._state = 'started'

        Process._this_process = self
        Process._counter = 0

        self.run()

        # help __del__ be called for each proxy 
        self.__dict__.clear()

    def start(self):
        assert self._state == 'initial'

        # It may be unsafe for the child process to use any proxies
        # from the parent process.  Therefore we pickle self.__dict__
        # and unpickle it in the child process
        from cPickle import loads, dumps
        data = dumps(self.__dict__, 2)
        save = {}
        retain = ('_group', '_target', '_name', '_state', '_identity')
        for i in self.__dict__.keys():
            save[i] = self.__dict__.pop(i)
            
        pid = os.fork()
        if pid == 0:
            self.__dict__.update(loads(data))
            self._run()
            os._exit(0)
        else:
            self.__dict__.update(save)
            self._pid = pid
            self._state = 'started'
            
    def setName(self, name):
        if self._state == 'initial':
            self._name = name
        else:
            raise NotImplementedError, 'cannot change name of started Process'

    def isAlive(self):
        raise NotImplementedError

    def isDaemon(self):
        return False

    def setDaemon(self):
        raise NotImplementedError
    
    def exit(n=0):
        os._exit(n)
    exit = staticmethod(exit)


class NonForkingProcess(Process):
    '''
    Analogue of threading.Thread which does not use os.fork
    '''

    _default_dir = os.path.dirname(sys.modules['os'].__file__)

    def start(self):
        assert self._state == 'initial'

        import binascii, cPickle, nonforking

        modulenames = {}

        for key, value in sys.modules.items():
            path = getattr(value, '__file__', None)
            if path is not None and not path.startswith(self._default_dir):
                modulenames[key] = path

        modulenames['__main__'] = os.path.abspath(sys.argv[0])

        names_to_files = binascii.hexlify(cPickle.dumps(modulenames, 2))
        _self = binascii.hexlify(cPickle.dumps(self, 2))

        self._pid = os.spawnv(
            os.P_NOWAIT, sys.executable,
            [sys.executable, nonforking.__file__, names_to_files, _self]
            )

        self._state = 'started'

    def exit(n=0):
        sys.exit(n)
    exit = staticmethod(exit)


if not hasattr(os, 'fork'):
    Process = NonForkingProcess


def currentProcess():
    '''
    Analogue of threading.currentThread
    '''
    return Process._this_process

del DummyProcess
