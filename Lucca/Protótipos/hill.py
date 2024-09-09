import numpy as np
import matplotlib.pyplot as plt

def hill(lim_x, lim_y, radiation):
  def perturb(x, y, e):
    pass

  def f(x, y):
    return np.exp(-(x**2)) + 3*np.exp(-((x-3)**2))

  x_axis = np.linspace(*lim_x)
  y_axis = np.linspace(*lim_y)
  plt.plot(x_axis, f(x_axis, y_axis))
  

  
  
hill([-2, 5], [-3, 5], 0.1)
plt.show()


