# pip install pandas sqlalchemy pymysql openpyxl numpy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Leitura dos dados da tabela tb_rodutos
df_estoque = pd.read_sql('tb_produtos', engine)

# Printando somente os 5 primeiros
print(df_estoque.head())

# Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

# Agrupando os produtos com o mesmo nome e somando as quantidades e valores
df_agrupado = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque': 'sum',
    'TotalEstoque': 'sum'
}).reset_index()

# Ordenando os produtos pelo total de estoque de forma decrescente
df_ordenado = df_agrupado.sort_values(by='TotalEstoque', ascending=False)

# Exibindo os produtos agrupados com o total de estoque
print(df_ordenado[['NomeProduto', 'TotalEstoque']])

# Calculando o total em dinheiro na soma de todos os produtos em estoque 
print(f'\nTotal geral em estoque: R$ {df_ordenado["TotalEstoque"].sum()}')


#  ------------------ MEDIDAS DE TENDÊNCIA CENTRAL ------------------

# Transformando o campo TotalEstoque em um array numpy
array_total_estoque = np.array(df_agrupado['TotalEstoque'])
# print(array_total_estoque)

# calculando a média
media = np.mean(array_total_estoque)
# Calculando a mediana
mediana = np.median(array_total_estoque)
# distancia entre a média e a mediana
distancia_media_mediana = abs((media - mediana) / mediana)

# Exibindo os resultados
print(f'Média do valor total: R$ {media:.2f}')
print(f'Mediana do valor total: R$ {mediana:.2f}')
print(f'Distância entre a média e a mediana: {distancia_media_mediana:.2f}')