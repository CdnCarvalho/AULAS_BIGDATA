
from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_loja2'

# cria a conexão com o banco de dados
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)

# printando somente os 5 primeiros
print(df_estoque.head())

# Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['Quantidade'] * df_estoque['Valor']

# Exibe o conteúdo das colunas
print(df_estoque[['Produto', 'TotalEstoque']])

# Calcula o valor do total do estoque
print(f'Total geral em estoque: R${df_estoque['TotalEstoque'].sum()}')


# Exporta o DataFrame para um arquivo CSV: utf-8-sig para abir no excel
df_estoque.to_csv('estoque_exportado.csv', sep=';', encoding='utf-8-sig', index=False)