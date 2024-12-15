import pandas as pd 
import numpy as np 

dados = pd.Series([2, 4, 6, 8, 10])

# Transforma os dados em array numpy
conjunto_dados = np.array(dados)

print(f'Conjunto de dados: {conjunto_dados}')

# Calcula a média
print(f'Média: {conjunto_dados.mean()}')

# Calcula a variância
print(f'Variância da série de dados: {np.var(conjunto_dados)}')

# Calcula o desvio padrão
# O desvio padrão é a raiz quadrada da variância.
print(f'Desvio Padrão da série de dados: {np.sqrt(conjunto_dados.var())}')

# Forma mais direta de calcular o desvio padrão
# Calcula diretamente o devio padrão do conjunto de dados
print(f'Desvio Padrão da série de dados: {np.std(conjunto_dados)}')

# Distância da variância da média: Variância / (Média^2)
distancia_var_media = np.var(conjunto_dados) / (conjunto_dados.mean() ** 2)
print(f'Distância da variância da média: {distancia_var_media}')

# Coeficiente de variação: Desvio padrão / Média
coef_variacao = (np.std(conjunto_dados) / conjunto_dados.mean()) * 100
