import mpi4py.MPI as MPI

# Type = { (double, 0), (char, 8) }

blens = (1, 1)
disps = (0, MPI.DOUBLE.size)
types = (MPI.DOUBLE, MPI.CHAR)

dtype = MPI.Datatype.Create_struct(blens, disps, types)
