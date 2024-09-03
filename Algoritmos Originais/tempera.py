import numpy as np
import matplotlib.pyplot as plt

def perturb(x,xl,xu,sigma):
    x_cand = x + np.random.normal(loc=0,scale=sigma)
    for i in range(x.shape[0]):
        if x_cand[i] < xl[i]:
            x_cand[i] = xl[i]
        if x_cand[i] > xu[i]:
            x_cand[i] = xu[i]
    return x_cand

def f(x,y):
    return x**2*np.sin(x*4*np.pi) - y*np.sin(4*np.pi*y+np.pi) + 1


x_axis = np.linspace(-1,2,1000)
X,Y = np.meshgrid(x_axis,x_axis)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,f(X,Y),cmap='gray',alpha=.3,edgecolor='k')

xl = [-1, -1]
xu = [2, 2]

x_opt = np.random.uniform(low=xl,high=xu)
f_opt = f(*x_opt)
ax.scatter(x_opt[0],x_opt[1],f_opt,marker='x',color='r',s=150,linewidth=3)
T = 100
it_max = 1000
sigma = .2
historico_f = [f_opt]
i = 0
while i < it_max:

    x_cand = perturb(x_opt,xl,xu,sigma)
    f_cand = f(*x_cand)
    p_ij = np.exp(-(f_cand-f_opt)/T)
    if f_cand < f_opt or p_ij >= np.random.uniform(0,1):
        x_opt = x_cand
        f_opt = f_cand
        ax.scatter(x_opt[0],x_opt[1],f_opt,marker='x',color='b',alpha=.3)
    historico_f.append(f_opt)
    i+=1
    T*=.89
    

ax.scatter(x_opt[0],x_opt[1],f_opt,marker='x',color='g',s=150,linewidth=3)
plt.show()

plt.plot(historico_f)
plt.show()