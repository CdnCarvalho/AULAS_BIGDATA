#  pip install pandas openpyxl
import pandas as pd
from sqlalchemy import create_engine

host = 'localhost'
user = 'root'
password = '123456'
database = 'exemplo3'

# Conexão com o banco de dados MySQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Carregar dados da tabela 'tb_clientes' do Banco Exemplo3 MySQL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, engine)

# Carregar dados da tabela 'pedidos' do arquivo Excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')

# Carregar dados da tabela 'produtos' do arquivo Excel
df_produtos = pd.read_excel('tb_produtos.xlsx')

# Relacionar os dados usando merge
df_relacionado = pd.merge(df_pedidos, df_clientes, on='id_cliente', how='inner')

# Relacionar os dados de pedidos com produtos
df_relacionado = pd.merge(df_relacionado, df_produtos, on='id_produto', how='inner')

# Ordenar o DataFrame relacionado pela coluna 'id_cliente'
df_relacionado = df_relacionado.sort_values(by='id_cliente')

# Exibir o resultado
print(df_relacionado)

