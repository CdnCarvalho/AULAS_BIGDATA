# import pandas as pd
# import numpy as np

dados = {1, 2, 3, 4, 5}

# Calcula a média
media = sum(dados) / len(dados)
print(f'Media: {media}')

# calcular as difernças entre cada valor e a média
diferencas = [x - media for x in dados]
print(f'Diferenças em relação a média: {diferencas}')

# elevar as diferenças ao quadrado
quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrados das diferenças: {quadrados_diferencas}')

# calcular a média dos quadrados das diferenças
media_quadrados_diferencas = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f'Variância é a média dos quadrados das diferenças: {media_quadrados_diferencas}')

# calcular a raiz quadrada da média dos quadrados das diferenças
desvio_padrao = media_quadrados_diferencas ** 0.5
print(f'Desvio padrão é a raiz quadrada da variância: {desvio_padrao}')

# Distância da variância em relação a média
distancia_varianc_media = media_quadrados_diferencas / (media ** 2)
print(f'Distância da variância em relação a média ao quadrado: {distancia_varianc_media}')

# O Percentual representativo
# Coeficiente de variação é o desvio padrão dividido pela média
coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de variação: {coef_variacao}')

