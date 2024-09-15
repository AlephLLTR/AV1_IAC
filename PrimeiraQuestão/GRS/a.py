import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, np.pi, 400)
y = np.linspace(0, np.pi, 400)
x, y = np.meshgrid(x, y)
z = (-np.sin(x) * (np.sin(x**2 / np.pi))**2 * 10**(-2)) - (np.sin(y) * (np.sin(2 * y**2 / np.pi))**2 * 10**(-2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title('3D Plot of the Given Equation (0 to π Range)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()