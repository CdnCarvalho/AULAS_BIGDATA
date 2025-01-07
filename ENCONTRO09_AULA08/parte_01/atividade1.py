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


# ######### PARA CÁLCULOS DE AMOSTRA  ############
# # Variância Cálculo - Amostra
# Uso do degrees of freedom (ddof) = 1
# O padrão do método numpy.var é calcular a variância Populacional. 
# Para calcular a variância Amostral ajustar o parâmetro ddof. 
# Esse parâmetro é definido como:
#    # População: ddof=0 (padrão no NumPy), ou seja, nem precisa escrevê-lo.
#    # Amostra: ddof=1.
variancia_amostral = np.var(dados, ddof=1)
print(f"Variância amostral: {variancia_amostral}")


# # Desvio Padrão - Amostra
# Faz se  uso do ddof=1.
# A explicação é a mesma da variância.
desvio_padrao_amostral = np.std(dados, ddof=1)
print(f'Desvio Padrão entre as idades: {desvio_padrao_amostral}')
