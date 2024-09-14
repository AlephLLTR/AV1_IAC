import numpy as np

def f(x1,x2):
  return -(x2 + 47) * np.sin(np.sqrt(abs(x1/2 + (x2 + 47)))) - x1 * np.sin(np.sqrt(abs(x1 + (x2 + 47))))

print(f(-5, 2))