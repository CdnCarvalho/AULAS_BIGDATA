# pip install mysql-connector-python
# pip install pandas
# pip install openpyxl

import mysql.connector
import pandas as pd

# Conexão com o banco de dados MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='exemplo3'
)

# Carregar dados da tabela 'tb_clientes' do Banco Exemplo3 MySQL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, db_connection)

# Carregar dados da tabela 'pedidos' do arquivo Excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')

# Relacionar os dados usando merge
df_relacionado = pd.merge(df_pedidos, df_clientes, on='id_cliente', how='inner')

# Ordenar o DataFrame relacionado pela coluna 'id_cliente'
df_relacionado = df_relacionado.sort_values(by='id_cliente')

# Exibir o resultado
print(df_relacionado)

# Fechar a conexão
db_connection.close()
