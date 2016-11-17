import numpy as np
import scikits.bvp1lg.colnew as colnew
import matplotlib.pyplot as plt
degrees=[2]

boundary_points = np.array([0,np.pi])
tol=1.0e-8*np.ones_like(boundary_points)

def fsub(x,Z):
    """The equations"""
    u,du=Z
    return np.array([-u])

def gsub(Z):
    """The boundary conditions"""
    u,du=Z
    return np.array([u[0]-0.0,du[1]-1])

solution=colnew.solve(
    boundary_points,degrees,fsub,gsub,
    is_linear=True,tolerances=tol,
    vectorized=True,
    maximum_mesh_size=300
    )



plt.ion()

x=solution.mesh

u_exact=-np.sin(x)

plt.plot(x,solution(x)[:,0],'b.')
plt.plot(x,u_exact,'g-')

plt.show()

