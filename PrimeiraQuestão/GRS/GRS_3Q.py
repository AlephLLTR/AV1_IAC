import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + 20 + np.e

    
fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
x_limits = [-8,8]
y_limits = [-8,8]

X = np.arange(*x_limits)
Y = np.arange(*y_limits)

X,Y = np.meshgrid(X,Y)

ax.plot_wireframe(X,Y,f(X,Y))

x_opt = x_limits[0]
y_opt = y_limits[0]
f_opt = f(x_opt,y_opt)
e = 10
max_it = 10000
max_viz = 50
i = 0
aux2=0
a = np.zeros(100)
for iterantions in range(100):
    melhoria = True
    while i<max_it and melhoria:
        melhoria = False
        for j in range(max_viz):
            x_cand = np.random.uniform(*x_limits)
            y_cand = np.random.uniform(*y_limits)
            f_cand = f(x_cand,y_cand)
            if f_cand < f_opt:
                x_opt = x_cand
                y_opt = y_cand
                f_opt = f_cand
                melhoria = True
                break
            i+=1
    a[aux2] = round(f_opt, 5)
    aux2 += 1
        # ax.scatter(x_opt,y_opt,f_opt, marker='X', color='r')
        # plt.pause(0.01)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

valores, aux3 = np.unique(a, return_counts=True)
moda = valores[np.argmax(aux3)]
print(f"mode_value: {moda}") 
# plt.show()