import unittest, tempfile
from mpi4py import MPI

class TestFileBase(object):

    COMM = MPI.COMM_NULL

    def setUp(self):
        self.FILE = None
        self.fname = tempfile.mktemp(prefix='mpi4py')
        self.amode = MPI.MODE_RDWR | MPI.MODE_CREATE
        #self.amode |= MPI.MODE_DELETE_ON_CLOSE
        try:
            self.FILE = MPI.File.Open(self.COMM,
                                      self.fname, self.amode,
                                      MPI.INFO_NULL)
        except NotImplementedError:
            return
        
    def tearDown(self):
        if self.FILE is None: return
        if self.FILE == MPI.FILE_NULL: return
        amode = self.FILE.amode
        self.FILE.Close()
        if not (amode & MPI.MODE_DELETE_ON_CLOSE):
            MPI.File.Delete(self.fname, MPI.INFO_NULL)

    def testPreallocate(self):
        if self.FILE is None: return
        self.FILE.Preallocate(0)
        size = self.FILE.Get_size()
        self.assertEqual(size, 0)
        self.FILE.Preallocate(100)
        size = self.FILE.Get_size()
        self.assertEqual(size, 100)
        self.FILE.Preallocate(10)
        size = self.FILE.Get_size()
        self.assertEqual(size, 100)
        self.FILE.Preallocate(200)
        size = self.FILE.Get_size()
        self.assertEqual(size, 200)

    def testGetSetSize(self):
        if self.FILE is None: return
        size = self.FILE.Get_size()
        self.assertEqual(size, 0)
        self.FILE.Set_size(100)
        size = self.FILE.Get_size()
        self.assertEqual(size, 100)

    def testGetGroup(self):
        if self.FILE is None: return
        fgroup = self.FILE.Get_group()
        cgroup = self.COMM.Get_group()
        gcomp = MPI.Group.Compare(fgroup, cgroup)
        self.assertEqual(gcomp, MPI.IDENT)

    def testGetAmode(self):
        if self.FILE is None: return
        amode = self.FILE.Get_amode()
        self.assertEqual(self.amode, amode)

    def testGetSetInfo(self):
        if self.FILE is None: return
        info = self.FILE.Get_info()
        self.FILE.Set_info(info)
        info.Free()

    def testGetSetView(self):
        if self.FILE is None: return
        fsize = 100 * MPI.DOUBLE.size
        self.FILE.Set_size(fsize)
        displacements = range(100)
        datatypes = [MPI.SHORT, MPI.INT, MPI.LONG, MPI.FLOAT, MPI.DOUBLE]
        datareps  = ['native'] #['native', 'internal', 'external32']
        for disp in displacements:
            for dtype in datatypes:
                for datarep in datareps:
                    etype, ftype = dtype, dtype
                    self.FILE.Set_view(disp, etype, ftype,
                                       datarep, MPI.INFO_NULL)
                    of, et, ft, dr = self.FILE.Get_view()
                    self.assertEqual(disp,    of)
                    self.assertEqual(etype,   et)
                    self.assertEqual(ftype,   ft)
                    self.assertEqual(datarep, dr)

    def testGetSetAtomicity(self):
        if self.FILE is None: return
        atom = self.FILE.Get_atomicity()
        self.assertFalse(atom)
        for atomicity in [True, False] * 4:
            self.FILE.Set_atomicity(atomicity)
            atom = self.FILE.Get_atomicity()
            self.assertEqual(atom, atomicity)

    def testSync(self):
        if self.FILE is None: return
        self.FILE.Sync()

    def testSeekGetPosition(self):
        if self.FILE is None: return
        offset = 0
        self.FILE.Seek(offset, MPI.SEEK_END)
        self.FILE.Seek(offset, MPI.SEEK_CUR)
        self.FILE.Seek(offset, MPI.SEEK_SET)
        pos = self.FILE.Get_position()
        self.assertEqual(pos, offset)
        
    def testSeekGetPositionShared(self):
        if self.FILE is None: return
        offset = 0
        self.FILE.Seek_shared(offset, MPI.SEEK_END)
        self.FILE.Seek_shared(offset, MPI.SEEK_CUR)
        self.FILE.Seek_shared(offset, MPI.SEEK_SET)
        pos = self.FILE.Get_position_shared()
        self.assertEqual(pos, offset)

    def testGetByteOffset(self):
        if self.FILE is None: return
        for offset in xrange(10):
            disp = self.FILE.Get_byte_offset(offset)
            self.assertEqual(disp, offset)

    def testGetTypeExtent(self):
        if self.FILE is None: return
        extent = self.FILE.Get_type_extent(MPI.BYTE)
        self.assertEqual(extent, 1)
        
    def testProperties(self):
        if self.FILE is None: return
        self.assertEqual(self.FILE.amode, self.amode)
        self.assertEqual(self.FILE.size,  0)
        

class TestFileSelf(TestFileBase, unittest.TestCase):
    COMM = MPI.COMM_SELF


if __name__ == '__main__':
    #unittest.main()
    try:
        unittest.main()
    except SystemExit:
        pass
