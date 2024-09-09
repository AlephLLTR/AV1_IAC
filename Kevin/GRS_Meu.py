import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(X):
    x1, x2 = X
    return x1**2 + x2**2

def grs (N_int, limites, dimencao):
    Melhor_solucao = 0
    M_valor = float('inf')
    solucao = []
    for i in range (N_int):
        candidato = np.random.uniform(limites[0], limites[1], size=(dimencao))
        candidato_v = f((candidato))
        solucao.append((candidato,candidato_v))
        if candidato_v < M_valor:
            M_valor = candidato_v
            Melhor_solucao = candidato
        print(f"Iteração {i+1}: Melhor valor até agora: {M_valor}")

    return Melhor_solucao, M_valor, solucao       

n_int = 100
limites = [-10, 10]
dimencao = 2

Melhor_solucao, M_valor, solucao = grs(n_int, limites, dimencao)

aux = plt.figure()
ax = aux.add_subplot(111, projection='3d')

X_val = np.array([s[0][0] for s in solucao])
Y_val = np.array([s[0][1] for s in solucao])
Z_val = np.array([s[1] for s in solucao])

ax.scatter(X_val, Y_val, Z_val, c='g', label='Soluções Aleatorias')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Valor da Função do objetivo')
plt.show()


