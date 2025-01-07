# Importa a biblioteca Pandas para manipulação de dados e a biblioteca NumPy para operações matemáticas e estatísticas
import pandas as pd
import numpy as np

# Carrega o arquivo Excel com os dados de vendas para um DataFrame (estrutura de dados similar a uma tabela)
df = pd.read_excel('vendas_roupas1.xlsx')

# Exibe o conteúdo do DataFrame para visualização geral dos dados
print(df)

# Seleciona a coluna 'Categoria' do DataFrame, que contém as categorias dos produtos
categoria = df['Categoria']

# Seleciona a coluna 'Quantidade Vendida', que contém as quantidades vendidas para cada produto
quantidade_vendida = df['Quantidade Vendida']

# Exibe a coluna 'Quantidade Vendida' para análise visual dos valores de quantidade vendida
print(quantidade_vendida)

# Exibe a coluna 'Categoria' para análise das categorias dos produtos
print(categoria)

# Calcula a média das quantidades vendidas e armazena o resultado na variável 'media'
media = np.mean(quantidade_vendida)

# Calcula a mediana das quantidades vendidas e armazena o resultado na variável 'mediana'
mediana = np.median(quantidade_vendida)

# Exibe a média das quantidades vendidas
print(f'Média: {media}')

# Exibe a mediana das quantidades vendidas
print(f'Mediana: {mediana}')

# Organiza o DataFrame em ordem crescente de 'Quantidade Vendida'
quantidadevdd_organizada = df.sort_values(by='Quantidade Vendida', ascending=True)

# Seleciona a coluna 'Quantidade Vendida' do DataFrame organizado
quantidade_vedida = quantidadevdd_organizada['Quantidade Vendida']

# Exibe os valores da coluna 'Quantidade Vendida' já organizados em ordem crescente
print(quantidade_vedida.values)
