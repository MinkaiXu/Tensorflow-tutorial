import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
x, y = np.meshgrid(X, Y)
R = np.sqrt(x**2+y**2)
z = np.sin(R)

# rstride/cstride: the range between two ticks
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
# offset: the tick where put the contourf
ax.contourf(x, y, z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()
