import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return  (-np.sin(x) * (np.sin(x**2 / np.pi))**2 * 10**(-2)) - (np.sin(y) * (np.sin(2 * y**2 / np.pi))**2 * 10**(-2))

def perturb(x,e):
     return np.random.uniform(low=x-e,high=x+e)

sigma = .1
N_max = 10000
a = np.zeros(100)
limites_x= [0, np.pi]
limites_y= [0, np.pi]

X = np.linspace(*limites_x)
Y = np.linspace(*limites_y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X,Y = np.meshgrid(X,Y)
ax.plot_surface(X,Y,f(X,Y), cmap='plasma')
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
          if f_cand < f_opt:
               f_opt = f_cand
               x_opt = x_cand
               y_opt = y_cand 
               melhoria = True
          i += 1
          ax.scatter(x_opt,y_opt,f_opt, marker='X', color='black')
          plt.pause(0.1)
     # a[aux2] = round(f_opt, 5)
     # aux2 += 1



ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# valores, aux3 = np.unique(a, return_counts=True)
# moda = valores[np.argmax(aux3)]
# print(f"mode_value: {moda}")  
plt.show() 
