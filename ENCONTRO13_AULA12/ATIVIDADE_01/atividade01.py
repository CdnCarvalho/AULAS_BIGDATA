import pandas as pd
import polars as pl
from datetime import datetime
import gc


CAMINHO_DADOS = r'./dados/'

try:
    print('Iniciando leitura do arquivo...')
    
    inicio = datetime.now()

    lista_arquivos = ['202403_NovoBolsaFamilia.csv', '202404_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f'Processasndo o arquivo {arquivo}')

        df_dados = pl.read_csv(CAMINHO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        print(df_dados)

        if r'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_dados])
        else:
            df_bolsa_familia = df_dados

        # Remover df_dados após o uso para liberar memória
        del df_dados
        # Forçar a coleta de lixo
        gc.collect()

    print('\nResultado')
    print(df_bolsa_familia)
    print(df_bolsa_familia.columns)

    fim = datetime.now()    
    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao importar os dados: {e}')