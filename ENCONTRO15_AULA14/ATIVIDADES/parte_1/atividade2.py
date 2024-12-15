# import pandas as pd
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

    # lista_arquivos = ['202404_NovoBolsaFamilia.csv', '202405_NovoBolsaFamilia.csv']

    lista_arquivos = []
    
    # Lista final dos arquivos de dados que vieram do diretório
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    # Pegando os arquivos CSVs do diretório
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # print(lista_arquivos)
    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')    

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        # limpar df da memória
        del df

        # coletar resíduos da memória
        gc.collect()

    print('Dataframes Concatenados com sucesso')

    # Converte a coluna 'VALOR PARCELA' para o tipo float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )

    print('\nDados dos DataFrames concatenados com sucesso!')
    
    print('Incinando a gravação do arquivo Parquet...')
    # Criar arquivo Parquet
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')  
    
    print(df_bolsa_familia)

    del df_bolsa_familia

    # coletar resíduos da memória
    gc.collect()

    fim = datetime.now()

    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao importar os arquivos: {e}')