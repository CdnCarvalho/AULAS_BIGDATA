from sqlalchemy import create_engine, text
import pandas as pd

host = 'localhost'
user = 'root'
password = '123456'
database = 'exemplo4_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
query = """SELECT * 
        FROM tb_clientes
        INNER JOIN tb_pedidos ON tb_clientes.id_cliente = tb_pedidos.id_cliente
        INNER JOIN tb_produtos ON tb_pedidos.id_produto = tb_produtos.id_produto;
        """

df_vendas = pd.read_sql(query, engine)
df_vendas_ordenadas = df_vendas.sort_values(by='nome', ascending=True)

# Eliminar colunas duplicadas, se houver
df_vendas_ordenadas = df_vendas_ordenadas.loc[:, ~df_vendas_ordenadas.columns.duplicated()]


print(df_vendas_ordenadas[['id_cliente', 'nome', 'email',
      'data_venda','id_pedido', 'qtd_comprada', 'id_produto', 'produto', 'categoria']])

# Verifique os nomes das colunas após o merge
print("Colunas no DataFrame após o merge:", df_vendas_ordenadas.columns)
