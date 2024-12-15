# pip install pandas sqlalchemy pymysql python-dotenv
# pip install python-dotenv


from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera as credenciais do banco de dados do arquivo .env
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

# Cria a conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)

# Printando somente os 5 primeiros registros
print(df_estoque.head())

# Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

# Exibe o nome do produto e o total do estoque por produto
print(df_estoque[['NomeProduto', 'TotalEstoque']])

# Calcula o valor total do estoque
print(f"Total geral em estoque: R${df_estoque['TotalEstoque'].sum()}")
