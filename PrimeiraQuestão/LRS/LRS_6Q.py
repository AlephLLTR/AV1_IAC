import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
   return x * np.sin(4 * np.pi * x) - y * np.sin(4 * np.pi * y + np.pi) + 1

def perturb(x,e):
     return np.random.uniform(low=x-e,high=x+e)

sigma = .1
N_max = 10000
a = np.zeros(100)
limites_x= [-1, 3]
limites_y= [-1, 3]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
X = np.linspace(*limites_x)
Y = np.linspace(*limites_y)
X,Y = np.meshgrid(X,Y)

surface = ax.plot_surface(X, Y, f(X,Y), cmap='viridis', edgecolor='none')
fig.colorbar(surface)
# ax.plot_wireframe(X,Y,f(X,Y))

x_opt = np.random.uniform(*limites_x)
y_opt = np.random.uniform(*limites_y)
f_opt = f(x_opt,y_opt)
i = 0
Max_i = 10
aux2 = 0
# for iterations in range(100):
melhoria = True
while i<Max_i and melhoria: 
     melhoria = False
     for j in range(N_max):
          x_cand = x_opt + np.random.uniform(-sigma, sigma)
          y_cand = y_opt + np.random.uniform(-sigma, sigma)
          np.clip(x_cand, *limites_x)
          np.clip(y_cand, *limites_y)
          f_cand=f(x_cand, y_cand)
          if f_cand > f_opt:
               f_opt = f_cand
               x_opt = x_cand
               y_opt = y_cand 
               melhoria = True
          ax.scatter(x_opt,y_opt,f_opt, marker='X', color='r')
          plt.pause(0.1)
          i += 1
# a[aux2] = round(f_opt, 5)
# aux2 += 1



ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# valores, aux3 = np.unique(a, return_counts=True)
# moda = valores[np.argmax(aux3)]
# print(f"mode_value: {moda}")   
plt.show()
