import numpy as np
import matplotlib.pyplot as plt

def canonicalGA(startingSize=4, stripSize=8, maxGenerations=1000, radiation=.1):

  def decoder(strip):
    output = 0
    for i, digit in enumerate(strip[::-1]):
      output += digit * 2**i
    return output

  def generateNewStrip(low=0, high=2):
    return np.random.randint(low, high, 8)

  def generateStartingPopulation(size=startingSize, ):
    P = np.empty((size, stripSize), dtype=int)
    for i in range(size):
      P[i] = generateNewStrip()
    return P

  def recombination(size, percentage):
    
    ...

  # def psi(self, x, nd, inf, sup):
  #   soma = 0
  #   for l in range(len(x)):
  #     soma += x[nd-1-1]*2**1
  #   return inf + (sup-inf)/(2**nd-1) * s

  # def f(self, x):
  #   A = 10
  #   s = 0
  #   for i in range(self.P):
  #     start = i* self.nd
  #     xi = self.psi(x[start:start+self.nd], self.nd, *self.limits)
  #     s += xi**2 - A*np.cos(2*np.pi*xi)
  #   return A*self.P+s+1

  def f(x=18, A=10, p=20):
    soma = 0
    for i in range(min(p, len(x))):
      soma += x[i]**2 - A * np.cos(2 * np.pi * x[i])
    return (A*p)+soma

  def selection(self):
    ...
  
  def crossover(self):
    ...

  def mutation(self):
    """_summary_
    """
    
    ...

  def fit():
    ...
    # return f(x)


  T = 0 # Gerações
  P = generateStartingPopulation()
  
  print(P[2],decoder(P[2]), f(P[2]))



  
  # for bin_number in P:
  #   dec_value = decoder(bin_number)
  #   print(f"Binary {bin_number} is equal to decimal {dec_value}")
 
 


canonicalGA()

