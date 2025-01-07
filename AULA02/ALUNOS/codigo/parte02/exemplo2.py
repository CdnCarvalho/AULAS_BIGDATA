# Importa a biblioteca NumPy, especializada em cálculos numéricos e operações com arrays
import numpy as np

# Definindo um array de dados com valores numéricos, que representam uma amostra de um conjunto de dados
dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

# Calcula o 1º quartil (Q1) - marca o ponto em que 25% dos dados são menores ou iguais a esse valor
q1 = np.percentile(dados, 25)

# Calcula o 2º quartil (Q2) - equivalente à mediana, onde 50% dos dados estão abaixo ou igual a este valor
q2 = np.percentile(dados, 50)

# Calcula o 3º quartil (Q3) - ponto em que 75% dos dados são menores ou iguais a esse valor
q3 = np.percentile(dados, 75)

# Exibe os valores dos quartis calculados
print("Q1:", q1)  # Exibe o 1º quartil
print("Q2:", q2)  # Exibe o 2º quartil (mediana)
print("Q3:", q3)  # Exibe o 3º quartil
