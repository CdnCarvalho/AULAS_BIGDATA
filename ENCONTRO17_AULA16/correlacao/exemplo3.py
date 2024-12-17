import polars as pl
from datetime import datetime

# Constante do Endereço dos dados
ENDERECO_DADOS = r'./dados/'


# obtendo dados do dados_bf.parquet
try:
    print('Obtendo dados....')

    hora_inicio = datetime.now()
    
    # Votação
    df_votacao = pl.read_csv(ENDERECO_DADOS + 'votacao_secao_2022_BR.csv', separator=';', encoding='iso-8859-1')

    hora_fim = datetime.now()
    print('Dados obtidos com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao obter dados: ', e)
    exit()


# iniciar processamento
try:
    print('Processando dados....')

    hora_inicio = datetime.now()   

    # filtrar NR_TURNO = 2 (Segundo Turno)
    # filtrar NR_VOTAVEL in [13, 22] (Número dos Candidatos)
    df_votacao = df_votacao.filter(
        (pl.col('NR_TURNO') == 2) &
        (pl.col('NR_VOTAVEL').is_in([13, 22]))
    )

    
    with pl.StringCache():
        '''VOTAÇÃO'''
        df_votacao_lazy = df_votacao.lazy().select(['SG_UF', 'NM_VOTAVEL', 'QT_VOTOS'])
        
        # Converter string para categórico
        df_votacao_lazy = df_votacao_lazy.with_columns([
            pl.col('SG_UF').cast(pl.Categorical),
            pl.col('NM_VOTAVEL').cast(pl.Categorical)
        ])

        # Agrupar qtd de votos. Totalizar por UF e candidato
        df_votacao_uf = df_votacao_lazy.group_by(['SG_UF', 'NM_VOTAVEL']).agg(pl.col('QT_VOTOS').sum())

        df_votacao_uf = df_votacao_uf.collect()


    # Exibir todas as linhas de um dataframe. Evitar em dados de larga escala
    pl.Config.set_tbl_rows(-1)
    print(df_votacao_uf)

    # formatação numérica para o valor parcela
    pl.Config.set_float_precision(2)
    pl.Config.set_decimal_separator(',')
    pl.Config.set_thousands_separator('.')

    hora_fim = datetime.now()
    print('Dados procesados com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao processar dados: ', e)
    exit()
