import unittest
from mpi4py import MPI

arrayimpl = []

try:
    import array
    mk_array = lambda typecode, init: array.array(typecode, init)
    eq_array = lambda a, b : a == b
    arrayimpl.append((mk_array, eq_array))
except ImportError:
    pass

try:
    import numpy
    mk_numpy = lambda typecode, init: numpy.array(init, dtype=typecode)
    eq_numpy = lambda a, b : (a == b).all()
    arrayimpl.append((mk_numpy, eq_numpy))
except ImportError:
    pass


typemap = dict(#b=MPI.CHAR,  #B=MPI.UNSIGNED_CHAR,
               h=MPI.SHORT, H=MPI.UNSIGNED_SHORT,
               i=MPI.INT,   I=MPI.UNSIGNED,
               l=MPI.LONG,  L=MPI.UNSIGNED_LONG,
               f=MPI.FLOAT, )# d=MPI.DOUBLE)

#typemap = dict(i=MPI.INT)
typemap = dict(h=MPI.SHORT)

class TestPackBase(object):

    COMM = MPI.COMM_NULL

    def testPackSize(self):
        for typecode, datatype in typemap.iteritems():
            itemsize = array.array(typecode).itemsize
            overhead = datatype.Pack_size(0, self.COMM)
            for count in xrange(10):
                pack_size = datatype.Pack_size(count, self.COMM)
                self.assertEqual(pack_size - overhead, count*itemsize)

    def testPackUnpack(self):
        for array, equal in arrayimpl:
            for items in xrange(10):
                for typecode1, datatype1 in typemap.iteritems():
                    for typecode2, datatype2 in typemap.iteritems():
                        # input and output arrays
                        iarray1 = array(typecode1, xrange(items))
                        iarray2 = array(typecode2, xrange(items))
                        oarray1 = array(typecode1, [items] * items)
                        oarray2 = array(typecode2, [items] * items)
                        # temp array for packing
                        size1 = datatype1.Pack_size(len(iarray1), self.COMM)
                        size2 = datatype2.Pack_size(len(iarray2), self.COMM)
                        tmpbuf = array('b', [0] * (size1 + size2 + 1))
                        # pack input arrays
                        position = 0
                        position = datatype1.Pack(iarray1, tmpbuf, position, self.COMM)
                        position = datatype2.Pack(iarray2, tmpbuf, position, self.COMM)
                        # unpack output arrays
                        position = 0
                        position = datatype1.Unpack(tmpbuf, position, oarray1, self.COMM)
                        position = datatype2.Unpack(tmpbuf, position, oarray2, self.COMM)
                        # test
                        self.assertTrue(equal(iarray1, oarray1))
                        self.assertTrue(equal(iarray2, oarray2))

EXT32 = 'external32'

class TestPackExternalBase(object):

    def testPackSize(self):
        try:
            MPI.BYTE.Pack_external_size(EXT32, 0)
        except NotImplementedError:
            return
        for typecode, datatype in typemap.iteritems():
            itemsize = array.array(typecode).itemsize
            overhead = datatype.Pack_external_size(EXT32, 0)
            for count in xrange(10):
                pack_size = datatype.Pack_external_size(EXT32, count)
                real_size = pack_size - overhead

    def testPackUnpackExternal(self):
        try:
            MPI.BYTE.Pack_external_size(EXT32, 0)
        except NotImplementedError:
            return
        for array, equal in arrayimpl:
            for items in xrange(1, 10):
                for typecode1, datatype1 in typemap.iteritems():
                    for typecode2, datatype2 in typemap.iteritems():
                        # input and output arrays
                        iarray1 = array(typecode1,[256] * items )#xrange(items))
                        iarray2 = array(typecode2, xrange(items))
                        oarray1 = array(typecode1, [items] * items)
                        oarray2 = array(typecode2, [items] * items)
                        # temp array for packing
                        size1 = datatype1.Pack_external_size(EXT32, len(iarray1))
                        size2 = datatype2.Pack_external_size(EXT32, len(iarray2))
                        tmpbuf = array('b', [0] * (size1 + size2 + 1))
                        # pack input arrays
                        position = 0
                        position = datatype1.Pack_external(EXT32, iarray1, tmpbuf, position)
                        position = datatype2.Pack_external(EXT32, iarray2, tmpbuf, position)
                        # unpack output arrays
                        position = 0
                        position = datatype1.Unpack_external(EXT32, tmpbuf, position, oarray1)
                        position = datatype2.Unpack_external(EXT32, tmpbuf, position, oarray2)
                        # test
                        if False: # Open MPI failed
                            if type(oarray1).__name__ == 'array':
                                oarray1.byteswap()
                                oarray2.byteswap()
                            else:
                                oarray1.byteswap(True)
                                oarray2.byteswap(True)
                        self.assertTrue(equal(iarray1, oarray1))
                        self.assertTrue(equal(iarray2, oarray2))
     
    
class TestPackSelf(TestPackBase, unittest.TestCase):
    COMM = MPI.COMM_SELF
    
class TestPackWorld(TestPackBase, unittest.TestCase):
    COMM = MPI.COMM_SELF

class TestPackExternal(TestPackExternalBase, unittest.TestCase):
    pass


if __name__ == '__main__':
    #unittest.main()
    try:
        unittest.main()
    except SystemExit:
        pass
