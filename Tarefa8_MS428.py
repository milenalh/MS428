import pandas as pd
import numpy as np
import matplotlib

def Simplex(Matriz_A, Vetor_B, Vetor_C, m, n): #Função Simplex de parâmetros 'Matriz_A, Vetor_B, Vetor_C, m, n'

    A = np.array(Matriz_A)
    b = np.array(Vetor_B)
    c = np.array(Vetor_C)

    B = np.zeros((m, m))
    N = np.zeros((m, n - m))
    c_B = np.zeros((m, 1))
    c_N = np.zeros((n - m, 1))
    Base = []
    Nao_Base = []
    Variaveis = []
    for i in range(n):
        Variaveis.append('x' + str(i + 1)) #variáveis x1, x2, x3,...

    def Fase_II(Base, Nao_Base):
        i = i + 1 # iteração
        B = A[:, Base] # pegar todas as linhas (:) das colunas da base
        c_B = c[Base, :] # pegar todas as colunas (:) das linhas da base

        N = A[:, Nao_Base] # pegar todas as linhas (:) das colunas da não base
        c_N = c[Nao_Base, :] # pegar todas as colunas (:) das linhas da não base

        # Passo 1: Cálculo da solução básica

        # Resolver o SL: B * x_B = b
        x_B = np.linalg.solve(B, b)

        # Calcular valor da função atual: f(x_B) = c_B^t * x_B 
        fx_B = np.dot(c_B, x_B)

        # Passo 2: Cálculo dos custos relativos

        # 2.1) Cálculo do vetor multiplicador simplex

        # Resolver o SL: B^t * lambda = c_B
        lbd = np.linalg.solve(B.T, c_B)

        # 2.2) Custos relativos
        N_j = [] # Lista dos custos relativos
        for i in range (len(Nao_Base)):
            # c_nj - lbd^t * a_nj
            N_j.append(c_N[i] - np.dot(lbd.T, N[:, i:i + 1])) 

        # 2.3) Escolha da variável a entrar na base
        N_j_min = min(N_j)

        # Passo 3: Teste da otimalidade
        if N_j_min >= 0:
            sol() #função para exibir resultados (?)
        
        # Passo 4: Cálculo da direção simplex
        else:
            
            # Resolver o SL: B * y = a_nk
            y = np.linalg.solve(B, ...) ## (B, coluna correspondente a variável do menor N_j)

        # Passo 5: Determinar variável a sair da base
        E_possiveis = []
        for i in range(len(y)):
            # Se y <= 0, então problema não tem solução ótima finita
            if y[i, 0] > 0:
                E_possiveis.append(x_B[i, 0] / y[i, 0])
            
            # Se há y > 0, então encontramos E (valor do passo)
            else:
                E = min(E_possiveis)

                # Passo 6: atualização: nova partição básica



