import numpy as N
import mpi4py.MPI as MPI

# extract the section a[0:6:2, 0:5:2] and store it in e[:,:]

a = N.empty((6, 5), dtype=float, order='fortran')
e = N.empty((3, 3), dtype=float, order='fortran')
a.flat = N.arange(a.size, dtype=float)

lb, sizeofdouble = MPI.DOUBLE.Get_extent()

# create datatype for a 1D section
oneslice = MPI.DOUBLE.Create_vector(3, 1, 2)

# create datatype for a 2D section
twoslice = oneslice.Create_hvector(3, 1, 12*sizeofdouble)
twoslice.Commit()

# send and recv on same process
myrank = MPI.COMM_WORLD.Get_rank()
status = MPI.Status()
MPI.COMM_WORLD.Sendrecv([a, 1, twoslice], myrank, 0,
                        (e, MPI.DOUBLE), myrank, 0, status)

assert N.allclose(a[::2, ::2], e)
assert status.Get_count(twoslice) == 1
assert status.Get_count(MPI.DOUBLE) == e.size

## oneslice.Free()
## twoslice.Free()

