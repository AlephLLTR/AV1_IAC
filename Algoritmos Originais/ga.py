class GeneticAlgorithm:
    def __init__(self,N,pm,pr,max_gen,psi,precision) -> None:
        pass

    def selection(self):
        ...
    
    def crossover(self):
        ...

    def mutation(self):
        ...

    def fit(self):
        ...
        
        
        
        
        
        
        
        
        
        
import numpy as np
        
def parte(tamanho, percentual):
    return np.floor((tamanho*percentual)/100)

print(parte(8, 85))