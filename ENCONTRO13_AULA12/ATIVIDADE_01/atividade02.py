import os
import pandas as pd
import polars as pl
from datetime import datetime
import gc


CAMINHO_DADOS = r'./dados/'

try:
    print('Iniciando leitura do arquivo...')
    
    inicio = datetime.now()

    # Lista final dos arquivos de dados que vieram do diretório
    lista_arquivos = []

    # Pegando os arquivos do diretório
    lista_dir_arquivos = os.listdir(CAMINHO_DADOS)

    # Adicionando cada arquivos CSV na lista final
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # Concatenando os dados de cada arquivo em um único DataFrame
    for arquivo in lista_arquivos:
        print(f'Processasndo o arquivo {arquivo}')

        df_dados = pl.read_csv(CAMINHO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        print(df_dados)

        # Verifica se o DataFrame df_bolsa_familia já existe,
        # Se existir, acontece a concatenação, 
        # Senão, (o Loop estpa na primeira execução), então
        # o df_dados é atribuído a df_bolsa_familia
        if r'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_dados])
        else:
            df_bolsa_familia = df_dados

        # Remover df_dados após o uso para liberar memória
        del df_dados
        # Forçar a coleta de lixo
        gc.collect()

        print(f'Arquivo {arquivo} processado com sucesso!')
    
    # Converte a coluna 'VALOR PARCELA' para o tipo float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )

    print('\nDados concatenados concatenados com sucesso!')
    print('Iniciando criação de arquivo Parquet')

    # Criando arquivo Parquet
    df_bolsa_familia.write_parquet(CAMINHO_DADOS + 'bolsa_familia.parquet')

    print('\nResultado')
    print(df_bolsa_familia)
    print(df_bolsa_familia.columns)

    # Deletando df_bolsa_familia após o uso para liberar memória
    del df_bolsa_familia
    # Coletar resíduos da memória
    gc.collect()
    fim = datetime.now()    
    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao importar os dados: {e}')
