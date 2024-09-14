import numpy as np
import matplotlib.pyplot as plt

def random_search(p=7, max_it = 10000):
  
  def perturb(x):
    return np.random.permutation(len(x))
  
  def f(cities, x):
    s = 0
    for i in range(len(x)):
      p1 = cities[x[i],:]
      p2 = cities[x[(i+1)%len(x)],:]
      s += np.linalg.norm(p1-p2)
    return s
  
  def starting_plot(cities, x):
    _,ax = plt.subplots()
    ax.scatter(cities[:,0], cities[:,1])
    lines = []
    
    for i in range(len(x)):
      p1 = cities[x[i],:]
      p2 = cities[x[(i+1)%len(x)],:]
      if i == 0:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='g')
      elif i == len(x)-1:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='r')
      else:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='k')
      lines.append(l[0])
      
    return lines, ax
  
  def update_plot(cities, x, lines, ax):
    plt.pause(.5)
    
    for line in lines:
      line.remove()
      
    for i in range(len(x)):
      p1 = cities[x[i],:]
      p2 = cities[x[(i+1)%len(x)],:]
      if i == 0:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color = 'g')
      elif i == len(x) - 1:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color = 'r')
      else:
        l = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color = 'k')
      lines[i] = l[0]
    
  cities = np.random.rand(p,2)
  
  x_opt = np.random.permutation(p)
  f_opt = f(cities, x_opt)
  lines,ax = starting_plot(cities, x_opt)
  
  for i in range(max_it):
    x_cand = perturb(np.copy(x_opt))
    f_cand = f(cities, x_cand)
    if f_cand < f_opt:
      f_opt = f_cand
      x_opt = x_cand
      update_plot(cities, x_opt, lines, ax)
      
  plt.show()
    
random_search()