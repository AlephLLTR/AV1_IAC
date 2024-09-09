# AV1 - Resolução de Problemas por Busca  

## Sobre o Trabalho

O Trabalho é dividido em três componentes diferentes

 ### 1. Problema de Minimização/Maximização de função Custo/Objetivo  
  - Utilizar algoritmos de **Hill Climbing**, **Local Random Search (LRS)** e **Global Random Search (GRS)** para solucionar problemas de dominio contínuo com espaço de estados infinito.
  
  - Cada problema consiste de elementos como:  
  
    - Função objetivo representando a quantidade a ser otimizada.
  
    - Conjunto de variáveis desconhecidas **x**. Onde f(x) quantifica a qualidade de uma solução.
  
    - Um conjunto de restrições limitando os valores possíveis das variáveis independentes, podem **excluir** soluções candidatas do conjunto de soluções.    
  
    Um problema de otimização irrestrito pode ser escrito tal qual:  
    ![Problema de otimização sem restrição](.arquivos/image.png)  
    Onde dom(xj) é o domínio da variável xj e para um problema contínuo, este domínio ´/ cada variável é conjunto dos reais (R).  
    
    #### Acerca da resolução de 1
    - Para cada algoritmo descrito anteriormente, projetar uma sequência de 100 rodadas onde cada rodada é composta por uma quantidade qualquer de **m** de iterações máximas, ao final do experimento, deve-se comport uma tabela com a moda de soluções de cada algoritmo.
    Outra definição importante para os algoritmos nesta seção é testar se um candidato gerado está no limite imposto pelas variáveis independendes (restrição de caixa). Também levar em consideração os hiperparâmetros específicos de cada algoritmo:  
    
    #### Hill Climbing  
      - Ponto Inicial ⬅ Limite inferior do domínio de **x**.
      - Para gerar um candidato a partir de **x_best** ⬅ **|x_best - y| <= ε**.  
      onde **y** é um possível candidato vizinho e ε deve ser definido com um valor inicial pequeno, 0.1 por exemplo.

      #### Busca Local Aleatória (LRS)  
      - Especificar o valor de desvio-padrão **0 < σ < 1**
      - Gerar candidato inicial x_best ⬅ número aleatório gerado por distribuição uniforme com limites impostos pelas variáveis independentes
      - Definir **σ** baseado na mesma visão da vizinhança do Hill CLimbing
      
      #### Busca Global Aleatória (GRS)  
      - Gerar um novo candidato ⬅ Gerado com distribuição uniforme com os limites impostos pelas variáveis independentes
      
    > Para os critérios de parada de cada algoritmo, definir uma qtd máxima de iterações em 10000 e também implementar uma possível parada antecipada ao verificar que não há melhoria na solução **x_best** a cada **t** iterações. Além disso, executar cada algoritmo **R** vezes


    #### Problemas à serem otimizados:  

    1. Considere as variáveis independentes **x = (x1, x2)**, encontre o valor **mínimo** da função:  
    f(x1,x2) = x1² + x2², em que o domínio das variáveis são x1, x2 ∈[−100,100]

    
    



## Documentação
- Algoritmos Originais: Inclui todos os algoritmos feitos em sala pelo professor que serão utilizados, modificados e adaptados para o trabalho.


## T0-DO
- Terminar de anotar o README.md
