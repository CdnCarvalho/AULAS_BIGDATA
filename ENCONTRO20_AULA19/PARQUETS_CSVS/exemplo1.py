# import pandas as pd
import polars as pl
from datetime import datetime
import os
import gc  # Garbage Collector
# from auxiliar.conexoes import obter_dados_pl 


ENDERECO_DADOS = r'./dados/'

try:
    print('Obtendo dados')

    inicio = datetime.now()

    # recebe os arquivos CSVs que serão verificados no for mais abaixo
    lista_arquivos = []
    
    # Lista dos arquivos de dados, que vierão do diretório
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    # Pegando os arquivos CSVs do diretório
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    df_bolsa_familia = None

    # Leitura dos arquivos
    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        # Leitura de cada um dos dataframes
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        # Concatenação dos Dataframes
        # Verifica se o DataFrame df_bolsa_familia já existe,
        # Se existir, acontece a concatenação, 
        # Senão, (o Loop estpa na primeira execução), então
        # o df_dados é atribuído a df_bolsa_familia
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        
        # Remover df_dados após o uso para liberar memória
        del df

        # Prints
        print(df_bolsa_familia)
        print(f'Arquivo {arquivo} processados com sucesso!')


    # Converte a coluna 'VALOR PARCELA' para o tipo float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )

    print('\nDados dos DataFrames concatenados com sucesso!')
    print('Incinando a gravação do arquivo Parquet...')

    # Criar arquivo Parquet
    # Um arquivo parquet é um arquivo de armazenamento de dados columnar
    # que permite leitura e gravação eficiente de dados.
    # estes dados são armazenados em um formato binário para melhor compactação,
    # o que permite uma leitura rápida e eficiente dos dados.
    # O arquivo parquet é um formato de arquivo de dados, que é amplamente
    # utilizado em big data e análise de dados em larga escala.
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Deletar df_bolsa_familia da memória
    del df_bolsa_familia
    
    # Coletar resíduos da memória
    gc.collect()

    fim = datetime.now()
    
    print(f'Tempo de execução: {fim - inicio}')
    print('Gravação do arquivo Parquet realizada com sucesso!')

except ImportError as e:
    print(f'Erro ao processar os dataframes: {e}')
