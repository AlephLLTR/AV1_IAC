import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as plt3d

def perturb(x, e):
  return np.random.uniform(low=x-e, high=x+e)

def f(x, y):
  return x*np.sin(10*np.pi*x) + y

x_axis, y_axis = np.meshgrid(np.linspace(*lim_x), np.linspace(*lim_y))
