import pandas as pd
from sqlalchemy import create_engine

# Variáveis de Conexão com o banco de dados MySQL
host = 'localhost'
user = 'root'
password = '123456'
database = 'atividade3'

# Cria a URL de conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Cria a query em SQL para pegar os dados da tabela de clientes
query_clientes = 'SELECT * FROM tb_clientes'

# Usa o métod read_sql com a conexão existente em engine para executar a query 
# e carregar os dados em um DataFrame
df_clientes = pd.read_sql(query_clientes, engine)
# print(df_clientes)

df_pedidos = pd.read_excel('tb_pedidos.xlsx')
# print(df_vendas)

# Realiza o Merge entre os DataFrames df_clientes e df_vendas
df_compras_clientes = pd.merge(df_clientes, df_pedidos, how='inner', on='id_cliente')

print(df_compras_clientes)
