import numpy as np
import matplotlib.pyplot as plt

def perturb(x, e):
  return np.random.uniform(x-e, x+e)

def f(x):
  return np.exp(-(x**2)) + 3*np.exp(-((x-3)**2))

limits = [-3,7]
x_axis = np.linspace(*limits) # o limite escolhido
plt.plot(x_axis, f(x_axis)) # desenha o gráfico

melhoria = True #assume-se que a melhoria é verdadeira no começo
x_opt = np.random.uniform(*limits) #x ótimo, valor arbitrário
f_opt = f(x_opt)
e = 0.1 #taxa de mutação
max_it = 100 #maximo de iterações
max_viz = 20 #máximo de vizinhos

while melhoria:
  melhoria = False #antes de checar, assumir que não houve melhoria
  for i in range(max_viz):
    x_cand = perturb(x_opt, e) #o x candidato será a perturbação do x ótimo
    f_cand = f(x_cand)
    if f_cand > f_opt: 
      x_opt = x_cand
      f_opt = f_cand
      melhoria = True
      break
    
  plt.scatter(x_opt, f_opt, marker='x')
  plt.pause(0.2)
  max_it -=1

plt.show()
bp = 0