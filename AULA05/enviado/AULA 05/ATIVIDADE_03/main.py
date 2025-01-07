import pandas as pd
from sqlalchemy import create_engine

# Variáveis de Conexão com o banco de dados MySQL
host = 'localhost'
user = 'root'
password = '123456'
database = 'atividade3'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Cria uma query em SQL para a tabela tb_clientes
query_clientes = 'SELECT * FROM tb_clientes'

# Usa a query, com a conexão com o banco de dados no pandas com o 
# método read_sql para criar um dataframe com todos os registros da 
# tabela de clientes existentes no banco de dados
df_clientes = pd.read_sql(query_clientes, engine)
# print(df_clientes)

# Realiza a leitura e carregamento da planilha de vendas do excel
# Openpyxl precisa está instalado
df_vendas = pd.read_excel('tb_vendas.xlsx')
# print(df_vendas)

# O métdo merge realiza a junção dos dois dataframes, com base em um campo em 
# comum, que é o id_cliente
df_compras_clientes = pd.merge(df_clientes, df_vendas, how='inner', on='id_cliente')

print(df_compras_clientes)