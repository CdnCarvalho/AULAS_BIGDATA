import polars as pl
from datetime import datetime

ENDERECO_DADOS = r'./dados/'

try:
    inicio = datetime.now()
    
    # Printando arquivo parquet
    print('Lendo dados do arquivo Parquet...')

    df_scanparquet = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = df_scanparquet.collect()

    print(df_bolsa_familia)

    fim = datetime.now()
    print(f'Atualização concluída! Tempo de execução: {fim - inicio}')

except ImportError as e:
    print("Erro na leitura do arquivo:", e)