import statistics

# 1- Aplicando a média - soma dos valores dividido pela quantidade de valores
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Aplicando a mediana - valor central de um conjunto de dados ordenados 
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))
print(statistics.median([90, 55, 307, 30, 91, 2])) # lista desordenada

# 3- Aplicando a moda - valor que mais se repete
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))

""" 4 - Desvio Padrão - medida que indica o quanto os valores
estão afastados da média do conjunto de dados
- Quanto mais próximo de 0 for o desvio padrão, significa que os
dados do conjunto estão menos dispersos em relação à média.
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))