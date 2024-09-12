import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return x**2 + y**2

def perturb(x,e):
     return np.random.uniform(low=x-e,high=x+e)

sigma = 10
N_max = 10000
a = np.zeros(N_max*100)
limites_x= [-100, 100]
limites_y= [-100, 100]

# fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
# X = np.arange(*limites_x)
# Y = np.arange(*limites_y)
# X,Y = np.meshgrid(X,Y)

# ax.plot_wireframe(X,Y,f(X,Y))
x_opt = np.random.uniform(*limites_x)
y_opt = np.random.uniform(*limites_y)
f_opt = f(x_opt,y_opt)

aux2 = 0
for iterations in range(100):
     for i in range(N_max):
          x_cand = x_opt + np.random.uniform(-sigma, sigma)
          y_cand = y_opt + np.random.uniform(-sigma, sigma)
          np.clip(x_cand, *limites_x)
          np.clip(y_cand, *limites_y)
          f_cand=f(x_cand, y_cand)
          if f_cand < f_opt:
               f_opt = f_cand
               x_opt = x_cand
               y_opt = y_cand 
          a[aux2] = round(f_opt, 5)
          aux2 += 1

#      ax.scatter(x_opt,y_opt,f_opt, marker='X', color='r')



# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
valores, aux3 = np.unique(a, return_counts=True)
i = 0 
for j in aux3:
     i = i +j
print(i)
moda = valores[np.argmax(aux3)]
print(f"mode_value: {moda}")   
