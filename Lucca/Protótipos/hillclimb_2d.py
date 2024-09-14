import numpy as np
import matplotlib.pyplot as plt

def hill(lim_x=[-100, 100], e=0.1, max_iterations=10000, max_neighbors=20, graph_color='g', s=50, linewidth=3, marker='x', pause=0.2):

  def perturb(x, e):
    return np.random.uniform(low=x-e, high=x+e)

  def f(x):
   return (x + np.sin(x))/x

  x_axis = np.linspace(*lim_x) #define o limite do gráfico
  plt.plot(x_axis, f(x_axis)) #desenha o gráfico
  
  optimized = True #assumir inicialmente que houve melhoria
  x_opt = np.random.uniform(*lim_x) #assumir um valor aleatório dentro dos limites de x para x_opt
  f_opt = f(x_opt)
  values = [f_opt]
  
  while optimized:
    optimized = False 
    for i in range(max_neighbors):
      x_candidate = perturb(x_opt, e)
      f_candidate = f(x_candidate)
      if f_candidate > f_opt:
        print(x_opt, f_opt)
        x_opt = x_candidate
        f_opt = f_candidate
        print(x_opt, f_opt)
        optimized = True
        break
    plt.scatter(x_opt, f_opt,color=graph_color, s=s, linewidth=linewidth, marker=marker)
    max_iterations -=1
    plt.pause(pause)
  
  plt.show()
hill()
