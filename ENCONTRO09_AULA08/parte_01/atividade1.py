import numpy as np


# Idade de 5 pessoas da mesma família
idades = [5, 10, 12, 35, 38]

dados = np.array(idades)
media = np.mean(dados)

print(f'Média: {media}')
      
# Variância Cálculo - População
variancia = np.var(dados)
print(f'Variância entre as idades: {variancia}')

# Desvio Padrão - População
desvio_padrao = np.std(dados)
print(f'Desvio Padrão entre as idades: {desvio_padrao}')

# Distância entre a Variância e a média
ditancia_var_media = variancia / (media ** 2)
print(f'Distância entre a Variância e a média: {ditancia_var_media}')

# Coeficiente de Variação
coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de Variação: {coef_variacao}')

# #########  AMOSTRA E POPULAÇÃO  ############
# # Variância Cálculo - Amostra
variancia_amostral = np.var(dados, ddof=1)
print(f"Variância amostral: {variancia_amostral}")


# # Desvio Padrão - Amostra
desvio_padrao_amostral = np.std(dados, ddof=1)
print(f'Desvio Padrão entre as idades: {desvio_padrao_amostral}')
