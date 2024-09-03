import numpy as np
import matplotlib.pyplot as plt

def perturb(x):
    # i1,i2 = np.random.permutation(len(x))[0:2]
    # x[i1],x[i2] = x[i2],x[i1]
    # return x
    return np.random.permutation(len(x))



def f(cidades,x):
    s = 0
    for i in range(len(x)):
        p1 = cidades[x[i],:]
        p2 = cidades[x[(i+1)%len(x)],:]
        s += np.linalg.norm(p1-p2)
    return s

def plot_inicial(cidades,x):
    _,ax = plt.subplots()
    ax.scatter(cidades[:,0],cidades[:,1])
    lines = []

    for i in range(len(x)):
        p1 = cidades[x[i],:]
        p2 = cidades[x[(i+1)%len(x)],:]
        if i == 0:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='g')
        elif i == len(x)-1:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='r')
        else:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='k')
        lines.append(l[0])
        
    return lines,ax

def atualiza_plot(cidades,x,lines,ax):
    plt.pause(.5)

    for line in lines:
        line.remove()

    for i in range(len(x)):
        p1 = cidades[x[i],:]
        p2 = cidades[x[(i+1)%len(x)],:]
        if i == 0:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='g')
        elif i == len(x)-1:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='r')
        else:
            l = ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='k')
        lines[i] = l[0]
    
    






p = 7

cidades = np.random.rand(p,2)


x_opt = np.random.permutation(p)
f_opt = f(cidades,x_opt)
lines,ax = plot_inicial(cidades,x_opt)

max_it = 10000

for i in range(max_it):
    x_cand = perturb(np.copy(x_opt))
    f_cand = f(cidades,x_cand)
    if f_cand < f_opt:
        f_opt = f_cand
        x_opt = x_cand
        atualiza_plot(cidades,x_opt,lines,ax)


plt.show()