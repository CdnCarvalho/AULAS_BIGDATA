# ATIVIDADE 2
from sqlalchemy import create_engine, text

host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_produtos'


# Função para verificar estoque baixo e gerar relatório de reabastecimento
def verificar_estoque_baixo():
    try:
        # Conectando ao banco de dados LojaVirtual usando SQLAlchemy e PyMySQL
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # Abrindo a conexão e executando a query
        with engine.connect() as conexao:
            print('Conectado ao banco de dados com sucesso!')
            # Definindo a query para buscar produtos com estoque inferior a 10
            query = "SELECT Country, Product, Port, Quantity FROM importacao WHERE Quantity < 2000;"

            # Executando a query e obtendo os resultados
            resultados = conexao.execute(text(query))

            # Verificando se há produtos com estoque baixo e exibindo os resultados
            if resultados.rowcount > 0:
                print("Produtos com estoque baixo:")
                for resultado in resultados:
                    print(f"País: {resultado[0]}, Produto: {resultado[1]}," 
                          f"Porto: {resultado[2]}, Estoque: {resultado[3]}")
            else:
                print("Nenhum produto com estoque baixo.")

    except ImportError as e:
        print(f"Erro ao verificar estoque: {e}")


# Chamando a função para executar a verificação de estoque baixo
verificar_estoque_baixo()
