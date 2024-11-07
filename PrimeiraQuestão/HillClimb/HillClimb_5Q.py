import numpy as np
import matplotlib.pyplot as plt

def perturb(x,e):
    return np.random.uniform(low=x-e,high=x+e)

def f(x,y):
    return x * np.cos(x) / 20 + 2 * np.exp((-x**2) - (y-1)**2) + 0.01 * x * y

    
fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
x_limits = [-10, 10]
y_limits = [-10, 10]

X = np.arange(*x_limits)
Y = np.arange(*y_limits)

X,Y = np.meshgrid(X,Y)

ax.plot_wireframe(X,Y,f(X,Y))

x_opt = x_limits[0]
y_opt = y_limits[0]
f_opt = f(x_opt,y_opt)
e = .1
a = np.zeros(100)
max_it = 10000
max_viz = 50
melhoria = True
i = 0
aux2 = 0
# for iterations in range(100):
while i<max_it and melhoria:
    melhoria = False
    for j in range(max_viz):
        x_cand = perturb(x_opt,e)
        y_cand = perturb(y_opt,e)
        f_cand = f(x_cand,y_cand)
        x_cand = np.clip(x_cand, *x_limits)
        y_cand = np.clip(x_cand, *x_limits)
        np.clip(y_cand, *y_limits)
        if f_cand > f_opt:
            x_opt = x_cand
            y_opt = y_cand
            f_opt = f_cand
            melhoria = True
            break
    i+=1
    ax.scatter(x_opt,y_opt,f_opt, marker='X', color='r')
    plt.pause(0.5)
# a[aux2] = round(f_opt, 5)
# aux2 += 1
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# valores, aux3 = np.unique(a, return_counts=True)
# moda = valores[np.argmax(aux3)]
# print(f"mode_value: {moda}") 
plt.show()