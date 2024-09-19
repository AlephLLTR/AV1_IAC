import numpy as np
from time import time

#Docstrings feitas em parte pelo ChatGPT

def decay_1(decay, T):
    """
    Aplica a taxa de decaimento à temperatura (T), seguindo o primeiro tipo de decaimento mostrado no slide.
    
    Parâmetros:
    decay (float): Fator de decaimento para reduzir a temperatura.
    T (float): Temperatura atual do sistema.

    Retorna:
    float: Nova temperatura após o decaimento. Temperatura x Decaimento
    """
    return T * decay

def decay_2(decay, T):
    """
    Aplica a taxa de decaimento à temperatura (T), segue o segundo tipo de decaimento mostrado no slide.
    
    Parâmetros:
    decay (float): Fator de decaimento para reduzir a temperatura.
    T (float): Temperatura atual do sistema.

    Retorna:
    float: Nova temperatura após o decaimento. Temperatura/(1 + decaimento + Temperatura²)
    """
    return T / (1 + decay * np.sqrt(T))


def queens(max_it=5000, alpha=0.79, defT=100, pick=4 ,output_file='queens_solutions.txt'):
    """
    Resolve o problema das 8 rainhas utilizando a técnica de recozimento simulado e salva as configurações aceitas (x_opt) em um arquivo.
    
    Parâmetros:
    max_it (int): Número máximo de iterações para a otimização (padrão: 5000).
    alpha (float): Fator de decaimento para a temperatura (padrão: 0.79).
    defT (int): Valor padrão de temperatura, auxiliar (padrão: 100). 
    pick (int): Quantidade de valores perturbados em um candidato x (padrão: 4).
    output_file (str): Caminho do arquivo onde as configurações de rainhas serão salvas.
    """
    
    def isUnique(x, hx):
        for h in hx:
            if np.array_equal(x, h):
                return False
        return True

    def perturb(x):
        """
        Gera uma perturbação na configuração atual trocando duas posições das rainhas no tabuleiro.
        
        Parâmetros:
        x (numpy array): Configuração atual das rainhas no tabuleiro.

        Retorna:
        numpy array: Nova configuração após a perturbação.
        """
        x_cand = np.copy(x)
        # print(x_cand)
        pos = np.random.choice(len(x), pick)
        x_cand[pos] = np.random.permutation(x_cand[pos])
        # print(x_cand)
        return x_cand

    def f(x):
        """
        Calcula a função de avaliação para a configuração das rainhas, onde o objetivo é minimizar o número de conflitos entre as rainhas.
        
        Parâmetros:
        x (numpy array): Configuração atual das rainhas no tabuleiro.

        Retorna:
        int: Valor da função de avaliação, sendo 28 o valor ideal (sem conflitos).
        """
        s = 0
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if x[i] == x[j] or abs(i - j) == abs(x[i] - x[j]):
                    s += 1
        return 28 - s

    def generateNewTable():
        """
        Gera uma nova configuração aleatória de rainhas no tabuleiro.
        
        Retorna:
        numpy array: Nova configuração de rainhas no tabuleiro.
        """
        return np.random.permutation(8)

    x_opt = generateNewTable() #Gera uma configuração inicial
    f_opt = f(x_opt) #Gera o f(x_opt) 
    history_x = [] #Inicializa o histórico de configurações únicas encontradas.
    possible = 92 
    i = 0
    T = defT #Temperatura inicial
    
    with open(output_file, 'w') as file:  # Abre o arquivo em modo de escrita
        while len(history_x) < 92:
            x_cand = perturb(x_opt)
            f_cand = f(x_cand)

            exponent = -(f_cand - f_opt) / T
            exponent = min(exponent, 700)
            exponent = max(exponent, -700)

            p_i = np.exp(exponent)

            if f_cand > f_opt or p_i < np.random.uniform(0, 1):
                x_opt = x_cand
                f_opt = f_cand

            T = decay_2(alpha, T)
            if T < 1e-10:
                T = 1e-10

            if f_opt == 28 or i >= max_it:
                if f_opt == 28:
                    # print('Accepted Table Configuration:')
                    # print('xopt  ', x_opt, ' fopt  ', f_opt, ' iterations ran ', i, ' remaining: ', possible)
                    
                    # Salva a configuração x_opt no arquivo
                    file.write(f"x_opt: {x_opt.tolist()}, f_opt: {f_opt}, iterations: {i}, remaining: {possible}\n")

                    if isUnique(x_opt, history_x):
                        possible -= 1
                        history_x.append(x_opt)

                x_opt = generateNewTable()
                f_opt = f(x_cand)
                i = 0
                T = defT
            i += 1
            
# Executa o algoritmo
i = 100
while i < 151:
    t0 = time()
    queens(defT=i)
    t1 = time()
    print(i, '|', t1-t0)
    i += 1
