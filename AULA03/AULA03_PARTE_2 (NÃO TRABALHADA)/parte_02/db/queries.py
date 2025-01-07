from sqlalchemy import text
from db.conexao import pegar_conexao


def pegar_todos_registros():
    engine = pegar_conexao()

    with engine.connect() as conexao:
        query = "SELECT * FROM base"
        resultados = conexao.execute(text(query))

        # return resultados.fetchall()
        for registro in resultados:
            print(f'id: {registro[0]}, Preço: {registro[1]}, Quantidade: {registro[2]}')
