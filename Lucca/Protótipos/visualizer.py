import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import Functions.func as fun

def view_3d(lim_x=fun.lim_xy_q3, lim_y=fun.lim_xy_q3, e=0, x_color='r', y_color='g', z_color='b', resolution=60, f=fun.f_q3):

  x_axis = np.linspace(*lim_x)
  y_axis = np.linspace(*lim_y)

  X, Y = np.meshgrid(x_axis, y_axis)
  z_axis = f(X, Y)

  fig = plt.figure()

  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(X, Y, z_axis, alpha=0.7, cmap=cm.turbo)

  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Z")

  plt.show()
  

def view_2d(lim_x=[-8,8], x_color='r'):
  def f(x):
    return -20 * np.exp(-0.2*np.sqrt(0.5*(x**2))) - np.exp(0.5*(np.cos(2*np.pi*x))) + 20 + np.exp(1)

  x_axis = np.linspace(*lim_x)

  fig = plt.figure()

  plt.plot(x_axis, f(x_axis), color=x_color)
  plt.show()


e = 0

while e < 10.1: 
  print(e)
  e+=0.1

# view_2d()
view_3d()
