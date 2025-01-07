# pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd

# variáveis de conexão
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_loja'

# Obtendo a conexão atráves da url de conexão atribuida a variável engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# leitura dos dados da tabela de produtos que está no banco de dados bd_loja
# Pandas usa o método próprio read_sql p/ se conectar, usando a engine com a 
# URL de conexão. Se tudo ocorrer bem, os dados são retornados em um DataFrame df_estoque
df_estoque = pd.read_sql('tb_produtos', engine)

# printando somente os 5 primeiros registros do DataFrame df_estoque
print(df_estoque.head())

# Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

print(df_estoque[['NomeProduto','TotalEstoque']])

# Calcula o valor do total existente na coluna estoque
print(f'Total geral em estoque: R${df_estoque['TotalEstoque'].sum()}')