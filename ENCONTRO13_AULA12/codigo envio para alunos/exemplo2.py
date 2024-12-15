import pandas as pd
import polars as pl
from datetime import datetime
import gc  #  Garbage Collector

ENDERECO_DADOS = r'./dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    lista_arquivos = ['202401_NovoBolsaFamilia.csv', '202402_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        # Se bolsa_familia já existir, concatena, senão, cria o dataframe bolsa familia
        # Estamos dentro do For. Na primeira iteração, não existe bolsa_familia
        # Na segunda iteração, existe bolsa_familia, então concatena
        if 'df_bolsa_falmilia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df

        # Prints
        print(df.head())
        # print(df.shape)
        # print(df.columns)
        # print(df.dtypes)

        # limpar df da memória
        del df        
        # coletar resíduos da memória
        gc.collect()

    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao importar os arquivos: {e}')