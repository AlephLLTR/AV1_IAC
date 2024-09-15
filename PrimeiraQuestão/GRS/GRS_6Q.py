import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
     return x * np.sin(4 * np.pi * x) - y * np.sin(4 * np.pi * y + np.pi) + 1
    
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
x_limits = [-1, 3]
y_limits = [-1, 3]
# linearEspace_limits = (-1, 3, 400)
linearEspace = np.linspace(-1,3)
linearEspace_Y = np.linspace(-1,3)
x_opt = x_limits[0]
y_opt = y_limits[0]
linearEspace,linearEspace_Y = np.meshgrid(linearEspace,linearEspace_Y)
f_opt = f(x_opt,y_opt)
surface = ax.plot_surface(linearEspace, linearEspace_Y, f(linearEspace,linearEspace_Y), cmap='viridis', edgecolor='none')
fig.colorbar(surface)


# ax.plot_wireframe(linearEspace,linearEspace_Y,f(linearEspace,linearEspace_Y))

e = 10
max_it = 10000
max_viz = 50
i = 0
aux2=0
a = np.zeros(100)
for iterantions in range(100):
    melhoria = True
    while i< max_it and melhoria:
        melhoria = False
        for j in range(max_viz):
            x_cand = np.random.uniform(*x_limits)
            y_cand = np.random.uniform(*y_limits)
            f_cand = f(x_cand,y_cand)
            if f_cand > f_opt:
                x_opt = x_cand
                y_opt = y_cand
                f_opt = f_cand
                melhoria = True
                break
            i+=1
    a[aux2] = round(f_opt, 5)
    aux2 += 1
        # ax.scatter(x_opt,y_opt,f_opt, marker='x', color='r')
        # plt.pause(0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

valores, aux3 = np.unique(a, return_counts=True)
moda = valores[np.argmax(aux3)]
print(f"mode_value: {moda}") 
# plt.show()