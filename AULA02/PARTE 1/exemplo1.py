import numpy as np  # Importa a biblioteca NumPy, que é útil para operações matemáticas e manipulação de arrays

# Lista de salários em uma moeda fictícia, representando uma pequena amostra de dados com um valor atípico (30000)
dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

# Calcula a média aritmética dos salários
# A média é sensível a valores atípicos, então o valor alto (30000) influencia este cálculo
media = np.mean(dados_salario)

# Calcula a mediana dos salários
# A mediana é o valor central e não sofre grande influência de valores extremos, 
# sendo útil para representar a posição central quando há valores atípicos
mediana = np.median(dados_salario)

# Exibe a média e a mediana
print('Média: ', media)       # Mostra o valor da média calculada
print('Mediana: ', mediana)    # Mostra o valor da mediana calculada