# Copyright (c) 2001-2004 Twisted Matrix Laboratories.
# See LICENSE for details.

import sys, pickle

try:
    import threading
except ImportError:
    threading = None

from twisted.trial import unittest
from twisted.python import threadable

class TestObject:
    synchronized = ['aMethod']

    x = -1
    y = 1

    def aMethod(self):
        for i in xrange(10):
            self.x, self.y = self.y, self.x
            self.z = self.x + self.y
            assert self.z == 0, "z == %d, not 0 as expected" % (self.z,)

threadable.synchronize(TestObject)

class SynchronizationTestCase(unittest.TestCase):
    if hasattr(sys, 'getcheckinterval'):
        def setUpClass(self):
            self.checkInterval = sys.getcheckinterval()
            sys.setcheckinterval(7)

        def tearDownClass(self):
            sys.setcheckinterval(self.checkInterval)

    def testThreadedSynchronization(self):
        o = TestObject()

        errors = []
        
        def callMethodLots():
            try:
                for i in xrange(1000):
                    o.aMethod()
            except AssertionError, e:
                errors.append(str(e))

        threads = []
        for x in range(5):
            t = threading.Thread(target=callMethodLots)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        if errors:
            raise unittest.FailTest(errors)

    def testUnthreadedSynchronization(self):
        o = TestObject()
        for i in xrange(1000):
            o.aMethod()

class SerializationTestCase(unittest.TestCase):
    def testPickling(self):
        lock = threadable.XLock()
        lockType = type(lock)
        lockPickle = pickle.dumps(lock)
        newLock = pickle.loads(lockPickle)
        self.failUnless(isinstance(newLock, lockType))

    def testUnpickling(self):
        lockPickle = 'ctwisted.python.threadable\nunpickle_lock\np0\n(tp1\nRp2\n.'
        lock = pickle.loads(lockPickle)
        newPickle = pickle.dumps(lock, 2)
        newLock = pickle.loads(newPickle)

if threading is None:
    SynchronizationTestCase.testThreadedSynchronization.skip = "Platform lacks thread support"
    SerializationTestCase.testPickling.skip = "Platform lacks thread support"
