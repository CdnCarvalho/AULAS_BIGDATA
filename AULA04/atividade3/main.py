import pandas as pd
import mysql.connector

# Conexão com o banco de dados MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='atividade3'
)

# Carregar dados da tabela 'clientes' do MySQL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, db_connection)

# Carregar dados da tabela 'produtos' do MySQL
query_produtos = "SELECT codigo_produto, produto, preco FROM tb_produtos"
df_produtos = pd.read_sql(query_produtos, db_connection)

# Carregar dados da tabela 'vendas' do arquivo Excel
df_vendas = pd.read_excel('tb_vendas.xlsx')

# Relacionar os dados usando merge
df_relacionado = pd.merge(df_vendas, df_clientes, on='id_cliente', how='inner')

df_relacionado = pd.merge(df_relacionado, df_produtos, on='codigo_produto', how='inner')

# Calcular o valor total da venda
df_relacionado['valor_total'] = df_relacionado['quantidade'] * df_relacionado['preco']

# Exibir o relatório final
print(df_relacionado[['nome', 'produto', 'quantidade', 'preco', 'data_venda', 'valor_total']])

# Fechar a conexão
db_connection.close()
