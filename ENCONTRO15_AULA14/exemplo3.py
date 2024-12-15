import polars as pl
from datetime import datetime
# import numpy as np
# from matplotlib import pyplot as plt


ENDERECO_DADOS = r'./dados/'

# LENDO OS DADOS DO ARQUIVO PARQUET
try:
    print('\nIniciando leitura do arquivo parquet...')

    # Pega o tempo inicial
    inicio = datetime.now()

    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') 
      
    # print(df_bolsa_familia)

    with pl.StringCache():
        # lazzy com delimitação das colunas. 
        # Dessa forma o df_bf continua com todas as colunas da fonte de dados
        df_bolsa_familia_lazy = df_bolsa_familia.lazy().select(['UF', 'VALOR PARCELA'])

        # converter UF para categórico
        df_bolsa_familia_lazy = df_bolsa_familia_lazy.with_columns(
            pl.col('UF').cast(pl.Categorical)
        )

        # totalizar valores
        df_bolsa_familia_lazy = df_bolsa_familia_lazy.group_by('UF').agg(pl.col('VALOR PARCELA').sum())

        # coletar dados
        df_bolsa_familia = df_bolsa_familia_lazy.collect()

        print(df_bolsa_familia)

    # Pega o tempo final
    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except ImportError as e: 
    print(f'Erro ao ler os dados do parquet: {e}')


try:
    print('\nIniciando leitura do arquivo parquet...')
    inicio = datetime.now()

    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Operações diretas sem categorização
    df_bolsa_familia_lazy = df_bolsa_familia.select(['UF', 'VALOR PARCELA'])
    df_bolsa_familia_lazy = df_bolsa_familia_lazy.group_by('UF').agg(pl.col('VALOR PARCELA').sum())
    # df_bolsa_familia = df_bolsa_familia_lazy.collect()

    print(df_bolsa_familia_lazy)

    fim = datetime.now()
    print(f'Tempo de execução: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except ImportError as e: 
    print(f'Erro ao ler os dados do parquet: {e}')
