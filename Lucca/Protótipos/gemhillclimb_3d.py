import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting

def hill(lim_x=[-100, 100], lim_y=[-100,100], e=0.1, max_iterations=10, 
         max_neighbors=5, graph_color='g', s=1, linewidth=1, marker='x', pause=0.2):
  
  def perturb(x, e):
    return np.random.uniform(low=x-e, high=x+e)

  def f(x1, x2):
    return (x1 + np.sin(x1))/x1

  # Create a mesh grid for x and y values
  X, Y = np.meshgrid(np.linspace(*lim_x), np.linspace(*lim_y))
  
  # Calculate Z values based on the function f(x, y)
  Z = f(X, Y)

  # Create a 3D plot
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Plot the surface using ax.plot_surface
  ax.plot_surface(X, Y, Z, color='b', alpha=0.5)  # Adjust color and transparency

  # Additional elements (optional):
  # ax.contour(X, Y, Z, zdir='z', offset=min(lim_y))  # Add contour lines
  # ax.scatter(X, Y, Z, color=graph_color, s=s, linewidth=linewidth, marker=marker)  # Plot individual points

  # Set axis labels and title
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('F(X, Y)')
  ax.set_title('3D Landscape of the Function')

  plt.show()

hill()