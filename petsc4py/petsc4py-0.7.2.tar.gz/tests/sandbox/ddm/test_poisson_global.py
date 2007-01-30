if __name__ == '__main__':
    import sys, petsc
    petsc.Init(sys.argv)
    del sys, petsc
    

import petsc.PETSc as PETSc


# ---------------------------------------------------

def Poisson3D(H, ndof, lgmap, gridshape):
 
    n0, n1, n2 = gridshape
    e0, e1, e2 = n0-1, n1-1, n2-1

    nodes = array.arange(n0*n1*n2, dtype=PETSc.Int).reshape(n0, n1, n2)

    icone = array.zeros((e0,e1,e2, 8))
    icone[:,:,:,0] = nodes[ 0:n0-1 , 0:n1-1, 0:n2-1 ]
    icone[:,:,:,1] = nodes[ 1:n0   , 0:n1-1, 0:n2-1 ]
    icone[:,:,:,2] = nodes[ 1:n0   , 1:n1  , 0:n2-1 ]
    icone[:,:,:,3] = nodes[ 0:n0-1 , 1:n1  , 0:n2-1 ]
    icone[:,:,:,4] = nodes[ 0:n0-1 , 0:n1-1, 1:n2   ]
    icone[:,:,:,5] = nodes[ 1:n0   , 0:n1-1, 1:n2   ]
    icone[:,:,:,6] = nodes[ 1:n0   , 1:n1  , 1:n2   ]
    icone[:,:,:,7] = nodes[ 0:n0-1 , 1:n1  , 1:n2   ]
    icone.shape = (e0*e1*e2, 8)
    icone = icone[:, [4,5,6,7,0,1,2,3]]

    elmat = [[ 4,  0, -1,  0,  0, -1, -1, -1],
             [ 0,  4,  0, -1, -1,  0, -1, -1],
             [-1,  0,  4,  0, -1, -1,  0, -1],
             [ 0, -1,  0,  4, -1, -1, -1,  0],
             [ 0, -1, -1, -1,  4,  0, -1,  0],
             [-1,  0, -1, -1,  0,  4,  0, -1],
             [-1, -1,  0, -1, -1,  0,  4,  0],
             [-1, -1, -1,  0,  0, -1,  0,  4]]
    elvec = [1] * 8

    elmat = 1.0/(12*H) * array.array(elmat, dtype=PETSc.Scalar)
    elvec = 1.0/8      * array.array(elvec, dtype=PETSc.Scalar)

    A = PETSc.MatMPIAIJ(ndof, d_nz=27, o_nz=9)
    x, b = A.getVecs()
    A.setLGMapping(lgmap)
    b.setLGMapping(lgmap)
    
    ADD_VALUES = PETSc.InsertMode.ADD_VALUES
    A_setValues = A.setValuesLocal
    b_setValues = b.setValuesLocal
    for elem in icone:
        A_setValues(elem, elem, elmat, ADD_VALUES)
        b_setValues(elem,       elvec, ADD_VALUES)
    A.assemble()
    b.assemble()
    return A, b, x


if __name__ != '__main__':
    import sys
    sys.exit(0)

import numpy.core as array

size = PETSc.WORLD_SIZE
rank = PETSc.WORLD_RANK


COMM = PETSc.COMM_WORLD

NDIM  = 3

#SHAPE = 3, 3, 3
#SHAPE = 5, 5, 5
#SHAPE = 10, 10, 10
SHAPE = 20, 20, 20
#SHAPE = 30, 30, 30
#SHAPE = 30, 30, 30

BBOX = [(0.0, 1.0)] * 3
PART  = 2, 2, 2

h =[(bb[1]-bb[0])/(SHAPE[i]-1)
    for i,bb in enumerate(BBOX)]
H = array.product(h)

from Grid import Grid
grid = Grid(SHAPE, bbox=BBOX, part=PART, pid=rank)

NDOF = array.product(SHAPE)
snodes = grid.nodes.copy()

## if rank == 0:
##     app, petsc = array.arange(NDOF), None
## else:
##     app, petsc = [], None
## aomap = PETSc.AOMapping(app, petsc)
## aomap.ApplicationToPetsc(snodes)

lgmap = PETSc.LGMapping(snodes, comm=COMM)
A, b, x = Poisson3D(H, NDOF, lgmap, snodes.shape)

if rank==0:
    bnd = [0], [0]
else:
    bnd = [], []
A.zeroRowsLocal(bnd[0])
b.setValuesLocal(bnd[0], bnd[1])
b.assemble()

ksp = PETSc.KSP(ksp_type='cg', pc_type='none', comm=COMM)
#ksp = PETSc.KSP(ksp_type='cg', pc_type='bjacobi', comm=COMM)
#ksp = PETSc.KSP(ksp_type='cg', pc_type='jacobi', comm=COMM)
#ksp = PETSc.KSP(ksp_type='cg', pc_type='nn', comm=COMM)

#ops['ksp_monitor'] = 'stdout'
ksp.setFromOptions()
ksp.guess_nonzero = True
ksp.max_it = 50

same_nz = PETSc.Mat.Structure.SAME_NONZERO_PATTERN
ksp.setOperators(A, A, same_nz)


from time import time

x.set(0)
t = time()
ksp.solve(b, x)
t = time()-t

PETSc.Print('its:%d,  time: %f\n'% (ksp.iternum, t))

x.set(0)
t = time()
ksp.solve(b, x)
t = time()-t

PETSc.Print('its:%d,  time: %f\n'% (ksp.iternum, t))

x.set(0)
t = time()
ksp.solve(b, x)
t = time()-t

PETSc.Print('its:%d,  time: %f\n'% (ksp.iternum, t))



loops = 5

if loops:
    PETSc.Print('---------------------------\n')
for i in xrange(loops):
    same_nz = PETSc.Mat.Structure.SAME_NONZERO_PATTERN
    ksp.setOperators(A, A, same_nz)
    x.set(0)
    ksp.solve(b, x)
    fmt = 'its:%d,  time: %f,  ||x||: %f, min(x): %s, max(x): %s\n'
    args = (ksp.iternum, t, x.norm(), x.min(), x.max())
    PETSc.Print(fmt % args)
