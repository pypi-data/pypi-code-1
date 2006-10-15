## mpiexec -n 4 python ex-2.16.py

# Jacobi code
# version of parallel code using sendrecv and null proceses.

# --------------------------------------------------------------------

import numpy
import mpi4py.MPI as MPI

# --------------------------------------------------------------------

n = 5 * MPI.WORLD_SIZE

# compute number of processes and myrank
p = MPI.COMM_WORLD.Get_size()
myrank = MPI.COMM_WORLD.Get_rank()

# compute size of local block
m = n/p
if myrank < (n - p * m):
    m = m + 1

#compute neighbors
if myrank == 0:
    left = MPI.PROC_NULL
else:
    left = myrank - 1
if myrank == p - 1:
    right = MPI.PROC_NULL
else:
    right = myrank + 1

# allocate local arrays
A = numpy.empty((n+2, m+2), dtype=float, order='fortran')
B = numpy.empty((n, m), dtype=float, order='fortran')

A.fill(1)
A[0, :] = A[-1, :] = 0
A[:, 0] = A[:, -1] = 0

# main loop
converged = False
while not converged:
    # compute,  B = 0.25 * ( N + S + E + W)
    N, S = A[:-2, 1:-1], A[2:, 1:-1]
    E, W = A[1:-1, :-2], A[1:-1, 2:]
    numpy.add(N, S, B)
    numpy.add(E, B, B)
    numpy.add(W, B, B)
    B *= 0.25
    A[1:-1, 1:-1] = B
    #communicate
    tag = 0
    MPI.COMM_WORLD.Sendrecv([B[:, -1], MPI.DOUBLE], right, tag,
                            [A[:,  0], MPI.DOUBLE], left,  tag)
    MPI.COMM_WORLD.Sendrecv((B[:,  0], MPI.DOUBLE), left,  tag,
                            (A[:, -1], MPI.DOUBLE), right, tag)
    # convergence
    myconv = numpy.allclose(B, 0)
    converged = MPI.COMM_WORLD.Allreduce(myconv, op=MPI.LAND)

# --------------------------------------------------------------------
