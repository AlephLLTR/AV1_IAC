import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
   return  -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_limits = [-200, 0]
y_limits = [-200, 0]

X = np.linspace(*x_limits)
Y = np.linspace(*y_limits)

X,Y = np.meshgrid(X,Y)

ax.plot_surface(X,Y,f(X,Y), cmap='magma')

x_opt = x_limits[0]
y_opt = y_limits[0]
f_opt = f(x_opt,y_opt)
e = 10
max_it = 10000
max_viz = 50
melhoria = True
i = 0
aux2=0
a = np.zeros(100)
for iterantions in range(100):
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
            ax.scatter(x_opt,y_opt,f_opt, marker='X', color='black')
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