import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

data = np.loadtxt('Snapshots/masset-velasco_fargo3d_448x1562_1e-4_0.1_alpha0.1_50_orbits.dat')
print(data.shape)
N = len(data[:,0])
x = data[:,0]
y = data[:,1]
rho = data[:,2]

triang = tri.Triangulation(x, y)
tri = plt.tripcolor(triang, rho, cmap='magma')
plt.gca().set_aspect('equal')
plt.show()
