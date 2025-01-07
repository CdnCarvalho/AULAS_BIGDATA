# EXEMPLO 2
# Importa as funções para criar uma conexão com o banco e formatar a query
from sqlalchemy import create_engine, text

# Variáveis de conexão com o banco de dados
host = 'localhost'         # Endereço do servidor onde o banco de dados está hospedado (aqui, na máquina local)
user = 'root'              # Nome do usuário do banco de dados (root é o padrão para MySQL)
password = 'root'        # Senha de acesso ao banco
database = 'bd_produtos'   # Nome do banco de dados, que contém as tabelas necessárias


# Função para conectar ao banco de dados. Esta função também executa uma consulta
def conecta_banco():
    try:
        # Cria o objeto de conexão com o banco de dados usando SQLAlchemy e PyMySQL.
        # Ele usa a URL de conexão formatada para MySQL (mysql+pymysql).
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # Estabelece a conexão com o banco de dados no contexto do bloco "with"
        # que garante que a conexão será fechada automaticamente após o uso
        with engine.connect() as conexao:
            # Define a query SQL para selecionar todos os registros da tabela "Base" e armazena dentro da variável "query".
            query = "SELECT * FROM Base"

            # 'text(query)' converte a string SQL em um objeto executável pelo SQLAlchemy
            # 'conexao.execute' envia a consulta ao banco e armazena o resultado em 'resultados'
            resultados = conexao.execute(text(query))

            # Laço para iterar pelos registros retornados do banco de dados pela query
            for item in resultados:
                # Imprime cada registro com informações formatadas:
                # item[0] é o primeiro campo, item[1] é o preço e item[2] é a quantidade
                print(f"{item[0]}, Preço: {item[1]}, Quantidade: {item[2]}")

    except ImportError as e:
        # Trata um erro de importação caso alguma biblioteca esteja faltando
        print(f"Erro capturado: {e}")


# Chama a função para estabelecer a conexão e executar a consulta
conecta_banco()
