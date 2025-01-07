# EXEMPLO 2
from sqlalchemy import create_engine, text

# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_produtos'


# Função para conectar ao banco
def conecta_banco():
    try:
        # URL de conexão com o banco, usando SQLAlchemy e PyMySQL
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # Estabelece a conexão
        with engine.connect() as conexao:
            # Query: "Linguagem SQL para selecionar todos os registros da tabela produtos"
            query = "SELECT * FROM base"

            # 'text(query)' transforma a string da query em um objeto compatível com SQLAlchemy.
            # 'conexao.execute' executa essa consulta no banco de dados.
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(f"Id: {item[0]}, Preço: {item[1]}, Quantidade: {item[2]}")

    except ImportError as e:
        print(f"Erro capturado: {e}")


# Chama função que conecta ao banco de dados
conecta_banco()
