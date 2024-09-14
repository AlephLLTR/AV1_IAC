import numpy as np
import matplotlib.pyplot as plt

def queens(low=1, high=9, max_it=100000, sigma=.2, T=100):

  def isUnique(x, hx):
    for h in hx:
      if np.array_equal(x, h):
        return False
    return True
  
  def isValid(f):
    return f == 28
  
  def perturb(x):
    x_cand = x + np.random.randint(low, high, 8)
    for i in range(x.shape[0]):
      if x_cand[i] < 1:
        x_cand[i] = np.random.randint(low, high*100/sigma)
      if x_cand[i] > 8:
        x_cand[i] = np.random.randint(low, high)
    # print(x_cand)
    return x_cand
  
  def f(x): # Calcula a qtd de pares atacantes
    s = 0
    for i in range(len(x)):
      for j in range(i+1, len(x)):
        if x[i] == x[j] or abs(i-j) == abs(x[i] - x[j]):
          s += 1
    return 28 - s
  
  def generateNewTable():
    return np.random.randint(low, high, 8)
  
  x_opt = generateNewTable()
  f_opt = f(x_opt)
  history_x = []
  possible = 92 #92 soluções possíveis
  i = 0
  
  while i < max_it:
    x_cand = perturb(x_opt)
    f_cand = f(x_cand)
    
    p_i = np.exp(-(f_cand-f_opt)/T)
    
    if f_opt < f_cand:
      x_opt = x_cand
      f_opt = f_cand
    elif f_cand < f_opt:
      x_opt = generateNewTable()
      f_opt = f(x_opt)
      
    if f_cand == 28:
      print('xcand  ', x_cand, ' fcand  ', f_cand)
      if isUnique(x_cand, history_x):
        history_x.append(x_cand)
        
    elif f_opt == 28:
      print('xopt  ', x_opt, ' fopt  ', f_opt)
      if isUnique(x_opt, history_x):
        history_x.append(x_opt)

        
      
      
    # if isValid(f_opt):
    #   return(x_opt)
      
    i+=1
    
  print('History: ', history_x)
  




































queens()


