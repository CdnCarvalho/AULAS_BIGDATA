import polars as pl
from datetime import datetime

# tempo 0:01:38.074710
ENDERECO_DADOS = r'./dados/'

# Lendo os dados do arquivo Parquet único
try:
    print('\nIniciando leitura do arquivo parquet...')

    inicio = datetime.now()

    # Gera um plano de execução
    df_auxilio = pl.scan_parquet(ENDERECO_DADOS + 'auxilio_emergencial.parquet') 
    # df_auxilio = df_auxilio.collect()

    # Coleta os dados do plano de execução
    print(df_auxilio.collect())

    fim = datetime.now()
    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')

    print('\nArquivo parquet lido com sucesso!')

except ImportError as e:
    print(f'Erro ao ler os dados do parquet: {e}')
