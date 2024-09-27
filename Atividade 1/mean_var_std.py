import numpy as np
# cria a função calculate que recebe uma lista de 9 números
def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    # transforma a lista em uma matriz 3x3
    matriz = np.array(lista).reshape(3, 3)
    # cria um dicionário com as operações que serão realiz
    calculations = {
        # calcula a média das colunas, das linhas e de toda a matriz
        'mean': [
            list(matriz.mean(axis=0)),
            list(matriz.mean(axis=1)),
            matriz.mean()               
        ],
        # calcula a variância das colunas, das linhas e de toda a matriz
        'variance': [
            list(matriz.var(axis=0)),
            list(matriz.var(axis=1)),
            matriz.var()
        ],
        # calcula o desvio padrão das colunas, das linhas e de toda a matriz
        'standard deviation': [
            list(matriz.std(axis=0)),
            list(matriz.std(axis=1)),
            matriz.std()
        ],
        # calcula o máximo das colunas, das linhas e de toda a matriz
        'max': [
            list(matriz.max(axis=0)),
            list(matriz.max(axis=1)),
            matriz.max()
        ],
        # calcula o mínimo das colunas, das linhas e de toda a matriz
        'min': [
            list(matriz.min(axis=0)),
            list(matriz.min(axis=1)),
            matriz.min()
        ],
        # calcula a soma das colunas, das linhas e de toda a matriz
        'sum': [
            list(matriz.sum(axis=0)),
            list(matriz.sum(axis=1)),
            matriz.sum()
        ]
    }



    return calculations