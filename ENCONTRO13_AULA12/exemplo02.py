import pandas as pd
import polars as pl
from datetime import datetime
import gc  #  Garbage Collector
# import os

# Pandas Tempo de execução: 0:01:09.272633 - 0:03:40.311191
# Polars Tempo de execução: 0:00:35.855072 - 0:00:44.743114

ENDERECO_DADOS = r'./dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    lista_arquivos = ['202401_NovoBolsaFamilia.csv', '202402_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        # Prints
        print(df)
        # print(df.shape)
        # print(df.columns)
        # print(df.dtypes)

        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df

        # limpar df da memória
        del df

        # coletar resíduos da memória
        gc.collect()

    print('Junção dos Dataframes do Novo Bolsa Família:')
    print(df_bolsa_familia)

    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao importar os arquivos: {e}')