import numpy as np

#Usei o ChatGPT pra documentar o código, tava com preguiça - Lucca

def print_chessboard(board):
    """
    Função de Exibição/Feita pelo ChatGPT
    Imprime o tabuleiro de xadrez de 8x8 onde a posição das rainhas é representada por 'Q' e espaços vazios por '.'.
    
    Parâmetros:
    board (list): Lista de 8 inteiros, onde cada valor representa a coluna em que uma rainha está posicionada
                  em cada linha (índice) do tabuleiro.
    """
    print("\n".join([" ".join(['Q' if board[i] == j else '.' for j in range(8)]) for i in range(8)]))
    print("\n" + "="*16 + "\n")

def decay_1(decay, T):
    """
    Aplica a taxa de decaimento à temperatura (T), importante no algoritmo de otimização simulada.
    
    Parâmetros:
    decay (float): Fator de decaimento para reduzir a temperatura.
    T (float): Temperatura atual do sistema.

    Retorna:
    float: Nova temperatura após o decaimento.
    """
    return T * decay

def queens(max_it=5000, alpha=0.79):
    """
    Resolve o problema das 8 rainhas utilizando a técnica de recozimento simulado (simulated annealing).
    O objetivo é encontrar todas as 92 configurações únicas onde 8 rainhas podem ser colocadas no tabuleiro sem atacar umas às outras.
    
    Parâmetros:
    max_it (int): Número máximo de iterações para a otimização (padrão: 5000).
    alpha (float): Fator de decaimento para controlar a redução da temperatura (padrão: 0.79).
    """
    
    def isUnique(x, hx):
        """
        Verifica se a configuração x é única em relação ao histórico de soluções (hx).
        
        Parâmetros:
        x (numpy array): Configuração atual das rainhas no tabuleiro.
        hx (list): Histórico de configurações já encontradas.

        Retorna:
        bool: True se x é único, False caso contrário.
        """
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
        pos = np.random.choice(len(x), 2)
        x_cand[pos] = np.random.permutation(x_cand[pos])
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

    x_opt = generateNewTable()  # Gera uma configuração inicial
    f_opt = f(x_opt)  # Calcula a função objetivo da configuração inicial
    history_x = []  # Histórico das configurações únicas encontradas
    possible = 92  # Número de soluções possíveis para o problema das 8 rainhas
    i = 0
    T = 100  # Temperatura inicial para o algoritmo de recozimento simulado

    # Loop principal do algoritmo
    while len(history_x) < 92:  # Continua até encontrar todas as 92 soluções
        x_cand = perturb(x_opt)  # Gera uma nova solução candidata
        f_cand = f(x_cand)  # Avalia a função objetivo da nova solução

        # Calcula a probabilidade de aceitação para o recozimento simulado
        exponent = -(f_cand - f_opt) / T
        exponent = min(exponent, 700)  # Limita o valor do expoente para evitar overflows numéricos
        exponent = max(exponent, -700)

        p_i = np.exp(exponent)  # Probabilidade de aceitar a solução pior

        # Condição para aceitar a nova solução
        if f_cand > f_opt or p_i < np.random.uniform(0, 1):
            x_opt = x_cand
            f_opt = f_cand

        # Aplica o decaimento na temperatura
        T = decay_1(alpha, T)
        if T < 1e-10:  # Define um limite inferior para a temperatura
            T = 1e-10

        # Verifica se a solução é a ótima ou se o número máximo de iterações foi alcançado
        if f_opt == 28 or i >= max_it:
            if f_opt == 28:  # Se for uma solução válida (f_opt == 28)
                print('Accepted Table Configuration:')
                print('xopt  ', x_opt, ' fopt  ', f_opt, ' iterations ran ', i, ' remaining: ', possible)
                print_chessboard(x_opt)  # Imprime o tabuleiro correspondente
                print('Iterations ran:', i, 'Remaining:', possible)

                # Verifica se a solução é única
                if isUnique(x_opt, history_x):
                    possible -= 1  # Reduz o número de soluções restantes
                    history_x.append(x_opt)  # Adiciona a solução ao histórico

            # Gera uma nova solução inicial para continuar a busca
            x_opt = generateNewTable()
            f_opt = f(x_cand)
            i = 0
            T = 100  # Reinicia a temperatura
        i += 1  # Incrementa o contador de iterações

# Executa o algoritmo
queens()
