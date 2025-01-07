from datetime import datetime
from auxiliar.conexoes import obter_dados_pl


ENDERECO_DADOS = r'./dados/csv/votacao/'

try:
    # hora de iníncio
    hora_import = datetime.now()

    # df_janeiro = pl.read_csv(ENDERECO_DADOS + '', separator=';', encoding='iso-8859-1')
    df_votacao = obter_dados_pl(ENDERECO_DADOS, 'votacao_secao_2022_BR.csv', 'csv', ';')

    print(df_votacao)
    # print(df_votacao.schema)
    for coluna, tipo in df_votacao.schema.items():
        print(f"Coluna: {coluna}, Tipo: {tipo}")


    # hora final
    hora_impressao = datetime.now()

    print(f"Tempo de execução: {hora_impressao - hora_import}")

except ImportError as e:
    print("Erro ao obter dados: ", e)
    exit()
