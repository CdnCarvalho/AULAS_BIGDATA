import polars as pl
from datetime import datetime



# Constante do Endereço dos dados
ENDERECO_DADOS = r'./dados/'


# obtendo dados do dados_bf.parquet
try:
    print('Obtendo dados....')

    hora_inicio = datetime.now()

    # Polars - Bolsa família
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    # Votação
    df_votacao = pl.read_csv(ENDERECO_DADOS + 'votacao_secao_2022_BR.csv', separator=';', encoding='iso-8859-1')

    # print(df_votacao)

    hora_fim = datetime.now()
    print('Dados obtidos com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao obter dados: ',e)
    exit()


# Iniciar processamento
try:
    print('Processando dados....')

    hora_inicio = datetime.now()   

    #filtrar NR_TURNO = 2
    # filtrar NR_VOTAVEL in [13,22]
    df_votacao = df_votacao.filter(
        (pl.col('NR_TURNO') == 2) &
        (pl.col('NR_VOTAVEL').is_in([13, 22]))
    )

    
    # Memória cache é a memória de acesso RÁPIDO
    # Ativar o método StringCache, do polars
    # Isso é muito útil para filtros, cálculos em dados de larga escala
    with pl.StringCache():

        '''VOTAÇÃO'''
        # lazzy com delimitação das colunas. 
        df_votacao_lazy = df_votacao.lazy().select(['SG_UF', 'NM_VOTAVEL', 'QT_VOTOS'])

        # Os tipos de dados categóricos são mais eficientes que a string
        # O Polar, qdo o tipo de dado é categórico, 
        # cria um dicionário de índices NUMÉRICOS, que otimiza o consumo de memória
        
        # Converter string para categórico
        df_votacao_lazy = df_votacao_lazy.with_columns([
            pl.col('SG_UF').cast(pl.Categorical),
            pl.col('NM_VOTAVEL').cast(pl.Categorical)
        ])

        # Agrupar qtd de votos. Totalizar por UF e candidato
        df_votacao_uf = df_votacao_lazy.group_by(['SG_UF','NM_VOTAVEL']).agg(pl.col('QT_VOTOS').sum())

        # Coleta os dados
        df_votacao_uf = df_votacao_uf.collect()


        '''BOLSA FAMÍLIA'''
        # lazzy com delimitação das colunas. 
        # Dessa forma o df_bolsa_familia continua com todas as colunas da fonte de dados
        df_bolsa_familia_uf_lazy = df_bolsa_familia.lazy().select(['UF', 'VALOR PARCELA'])

        # converter UF para categórico
        df_bolsa_familia_uf_lazy = df_bolsa_familia_uf_lazy.with_columns(pl.col('UF').cast(pl.Categorical))

        # Totalizar o valor das parcelas por estado
        df_bolsa_familia_uf = df_bolsa_familia_uf_lazy.group_by('UF').agg(pl.col('VALOR PARCELA').sum())

        # Coletar dados
        df_bolsa_familia_uf = df_bolsa_familia_uf.collect()

        # Juntar os dois dataframes. Faz o mesmo que o merge() do Pandas
        '''JOIN DOS DATAFRAMES'''
        df_votos_bolsa_familia = df_votacao_uf.join(df_bolsa_familia_uf, left_on='SG_UF', right_on='UF')
    

    # Exibir todas as linhas de um dataframe. Evitar em dados de larga escala
    pl.Config.set_tbl_rows(-1)
    print(df_votacao_uf)

    # formatação numérica para o valor parcela
    pl.Config.set_float_precision(2)
    pl.Config.set_decimal_separator(',')
    pl.Config.set_thousands_separator('.')

    print(df_bolsa_familia_uf)

    print(df_votos_bolsa_familia)

    hora_fim = datetime.now()
    print('Dados procesados com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao processar dados: ', e)
    exit()
