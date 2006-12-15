from petsc4py import PETSc
import unittest

# --------------------------------------------------------------------

class TestVecBase(object):

    CLASS = None
    TARGS = []
    KARGS = {}
    
    def setUp(self):
        v = PETSc.Vec()
        v.create()
        v.setSizes(100)
        v.setType(self.CLASS.TYPE)
        self.vec = v
        # self.vec = self.CLASS(v, *self.TARGS, **self.KARGS)
        
    def tearDown(self):
        self.vec.destroy()
        self.vec = None

    def testDuplicate(self):
        self.vec.set(1)
        vec = self.vec.duplicate()
        self.assertFalse(self.vec.equal(vec))
        self.assertEqual(self.vec.sizes, vec.sizes)
        del vec

    def testCopy(self):
        self.vec.set(1)
        vec = self.vec.duplicate()
        self.vec.copy(vec)
        self.assertTrue(self.vec.equal(vec))
        del vec

    def testDot(self):
        self.vec.set(1)
        d = self.vec.dot(self.vec)
        self.assertAlmostEqual(abs(d), self.vec.getSize())
        self.vec.dotBegin(self.vec)
        d = self.vec.dotEnd(self.vec)
        self.assertAlmostEqual(abs(d), self.vec.getSize())

    def testNorm(self):
        from math import sqrt
        self.vec.set(1)
        n1 = self.vec.norm(PETSc.NormType.NORM_1)
        n2 = self.vec.norm(PETSc.NormType.NORM_2)
        ni = self.vec.norm(PETSc.NormType.NORM_INFINITY)
        self.assertAlmostEqual(n1, self.vec.getSize())
        self.assertAlmostEqual(n2, sqrt(self.vec.getSize()))
        self.assertAlmostEqual(n2, self.vec.norm())
        self.assertAlmostEqual(ni, 1.0)
        self.vec.normBegin(PETSc.NormType.NORM_1)
        nn1 = self.vec.normEnd(PETSc.NormType.NORM_1)
        self.assertAlmostEqual(nn1, n1)
        self.vec.normBegin()
        nn2 = self.vec.normEnd()
        self.assertAlmostEqual(nn2, n2)
        self.vec.normBegin(PETSc.NormType.NORM_INFINITY)
        nni = self.vec.normEnd(PETSc.NormType.NORM_INFINITY)
        self.assertAlmostEqual(nni, ni)
        
    def testSumMinMax(self):
        self.vec.set(1)
        self.assertEqual(self.vec.sum(), self.vec.getSize())
        self.vec.set(-7)
        self.assertEqual(self.vec.min()[1], -7)
        self.vec.set(10)
        self.assertEqual(self.vec.max()[1], 10)
    
    def testNormalize(self):
        from math import sqrt
        self.vec.set(1)
        n2 = self.vec.normalize()
        self.assertAlmostEqual(n2, sqrt(self.vec.getSize()))
        self.assertAlmostEqual(1, self.vec.norm())

    def testSwap(self):
        v1 = self.vec
        v2 = v1.duplicate()
        v1.set(1)
        v2.set(2)
        v1.swap(v2)
        idx, _ = self.vec.getOwnershipRange()
        self.assertEqual(v1[idx], 2)
        self.assertEqual(v2[idx], 1)

    def testBsize(self):
        self.vec.setBlockSize(1)
        self.assertEqual(self.vec.getBlockSize(), 1)
        self.vec.setBlockSize(1)

    def testGetSetVals(self):
        start, end = self.vec.getOwnershipRange()
        self.vec[start] = -7
        self.vec[end-1]   = -7
        self.assertEqual(self.vec[start], -7)
        self.assertEqual(self.vec[end-1], -7)
        self.vec[start:end] = xrange(start, end)
        values = list(self.vec[start:end])
        self.assertEqual(values, range(start, end))
        sz = self.vec.getSize()
        self.assertEqual(self.vec.sum(), (sz-1)/2.0*sz)

    def testGetSetValsBlocked(self):
        lsize, gsize = self.vec.getSizes()
        start, end = self.vec.getOwnershipRange()
        bsizes  = range(1, lsize+1)
        nblocks = range(1, lsize+1)
        compat = [(bs, nb)
                  for bs in bsizes  if not (gsize%bs or lsize % bs)
                  for nb in nblocks if bs*nb <= lsize]
        for bsize, nblock in compat:
            self.vec.setBlockSize(bsize)
            bindex = [start//bsize+i  for i in xrange(nblock)]
            bvalue = [float(i) for i in xrange(nblock*bsize)]
            self.vec.setValuesBlocked(bindex, bvalue)
            self.vec.assemble()
            index = [start+i for i in xrange(nblock*bsize)]
            value = self.vec.getValues(index)
            self.assertEqual(bvalue, list(value))

    def testGetSetArray(self):
        self.vec.set(1)
        arr0 = self.vec.getArray()
        self.assertEqual(arr0.sum(), self.vec.getLocalSize())
        self.vec.getArray(arr0)
        self.vec.setRandom()
        arr1 = self.vec.getArray()
        self.vec.setArray(arr1)
        self.vec.getArray(arr1)
        arr2 = self.vec.getArray()
        self.assertTrue((arr1 == arr2).all())
        import numpy
        refs = self.vec.getRefCount()
        arr3 = numpy.asarray(self.vec)
        self.assertEqual(self.vec.getRefCount(), refs)
        self.assertTrue((arr1 == arr3).all())
        arr3[:] = 0
        self.assertAlmostEqual(abs(self.vec.sum()), 0)
        self.assertEqual(self.vec.max()[1], 0)
        self.assertEqual(self.vec.min()[1], 0)
        self.vec.set(1)
        self.assertAlmostEqual(abs(arr3.sum()), self.vec.getLocalSize())
        self.assertEqual(arr3.min(), 1)
        self.assertEqual(arr3.max(), 1)
        del arr3
        self.assertEqual(self.vec.getRefCount(), refs)
        
    def testPlaceArray(self):
        self.vec.set(1)
        array = self.vec.getArray()
        self.vec.placeArray(array)
        array[:] = 2
        self.assertAlmostEqual(abs(self.vec.sum()), 2*self.vec.getSize())
        self.vec.resetArray()
        self.assertAlmostEqual(abs(self.vec.sum()), self.vec.getSize())
        
# --------------------------------------------------------------------

class TestVecSeq(TestVecBase, unittest.TestCase):
    CLASS = PETSc.VecSeq

class TestVecMPI(TestVecBase, unittest.TestCase):
    CLASS = PETSc.VecMPI

class TestVecShared(TestVecBase, unittest.TestCase):
    if PETSc.COMM_WORLD.getSize() == 1:
        CLASS = PETSc.VecShared
    else:
        CLASS = PETSc.VecMPI

#class TestVecSieve(TestVecBase, unittest.TestCase):
#    CLASS = PETSc.VecSieve
#    TARGS = ([],)

#class TestVecGhost(TestVecBase, unittest.TestCase):
#    CLASS = PETSc.VecGhost
#    TARGS = ([],)
    
# --------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
