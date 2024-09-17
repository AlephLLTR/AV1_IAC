import numpy as np
import matplotlib.pyplot as plt

def decay_1(decay, T):
    return T * decay

def decay_2(decay, T):
    return T/(1 + decay * np.sqrt(T))

def decay_3(T, To, Tnt, nt):
    return T - (To - Tnt)/nt
    
def queens(max_it=5000, alpha= 0.79):

    def isUnique(x, hx):
        for h in hx:
            if np.array_equal(x, h):
                return False
        return True

    def perturb(x):
        x_cand = np.copy(x)
        pos = np.random.choice(len(x), 2)
        x_cand[pos] = np.random.permutation(x_cand[pos])
        return x_cand 

    def f(x): 
        s = 0
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                if x[i] == x[j] or abs(i-j) == abs(x[i] - x[j]):
                    s += 1
        return 28 - s

    def generateNewTable():
        return np.random.permutation(8)

    x_opt = generateNewTable()
    f_opt = f(x_opt)
    history_x = []
    possible = 92  # 92 possible solutions
    i = 0
    T = 100
    
    while len(history_x) < 92:
        x_cand = perturb(x_opt)
        f_cand = f(x_cand)

        p_i = np.exp(-(f_cand-f_opt)/T)

        if f_cand > f_opt or p_i < np.random.uniform(0, 1):
            x_opt = x_cand
            f_opt = f_cand
            
        T = decay_1(alpha, T)
        
        if f_opt == 28 or i >= max_it:
            if f_opt == 28:
                print('xopt  ', x_opt, ' fopt  ', f_opt, ' iterations ran ', i, ' remaining: ', possible)
                if isUnique(x_opt, history_x):
                    possible -= 1
                    history_x.append(x_opt)
            x_opt = generateNewTable()
            f_opt = f(x_cand)
            i = 0
            T = 100
        i += 1

    # print('History: ', history_x)

queens()