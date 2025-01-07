# Importa as bibliotecas Pandas e NumPy para manipulação de dados e cálculos estatísticos
import pandas as pd
import numpy as np

# Carrega os dados do arquivo Excel em um DataFrame para análise
df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')

# **Medidas de Posição**
# Cálculo das medidas de tendência central

# Calcula a média dos valores totais de vendas
media_preco = np.mean(df['Total'])

# Calcula a mediana dos valores totais de vendas
mediana_preco = np.median(df['Total'])

# **Obtendo os Quartis**
# Extrai os quartis para a coluna 'Total' (valores totais de vendas)
q1 = np.percentile(df['Total'], 25)  # Primeiro quartil (25%)
q2 = np.percentile(df['Total'], 50)  # Segundo quartil ou mediana (50%)
q3 = np.percentile(df['Total'], 75)  # Terceiro quartil (75%)

# **Filtragem de Produtos Mais Vendidos**
# Filtra os produtos cuja venda total (coluna 'Total') é maior que o terceiro quartil (top 25% mais vendidos)
produtos_mais_vendidos = df[df['Total'] > q3]

# Exibição dos resultados

# Linha separadora para organização visual
print(70 * '_')

# Exibe as medidas de tendência central (média e mediana dos preços totais)
print(f'\nMEDIDAS DE TENDÊNCIA CENTRAL')
print(f"Média dos preços: R$ {media_preco:.2f}")
print(f"Mediana dos preços: R$ {mediana_preco:.2f}")

# Linha separadora para organização visual
print(70 * '_')

# Exibe os quartis para análise detalhada dos valores de vendas
print(f'\nANÁLISE DOS VALORES: QUARTIS')
print(f"25% das vendas tiveram o valor total arrecadado até: R$ {q1:.2f}")
print(f"50% da arrecadação total dos produtos vendidos foi abaixo ou igual a: R$ {q2:.2f}")
print(f"75% do total das vendas ficaram abaixo de: R$ {q3:.2f}")

# Linha separadora para organização visual
print(70 * '_')

# Exibe os produtos mais vendidos (aqueles no quarto quartil, acima de Q3), ordenados do maior para o menor valor total
print(f'\nPRODUTOS MAIS VENDIDOS: QUARTIL')
print(produtos_mais_vendidos[['Nome do Produto', 'Total']].sort_values(by='Total', ascending=False))
