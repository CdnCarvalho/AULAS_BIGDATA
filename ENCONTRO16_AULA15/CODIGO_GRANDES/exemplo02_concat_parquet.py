import os
import gc
from datetime import datetime
import polars as pl

# Tempo de execução: 0:04:06.770102

ENDERECO_DADOS = './dados/'
ARQUIVO_FINAL = './dados/auxilio_emergencial.parquet'

# Concatena os arquivos Parquet em um único arquivo
try:
    print('Processando...')

    inicio = datetime.now()

    # Adiciona todos os arquivos .parquet na lista acima
    arquivos_parquet = []
    for f in os.listdir(ENDERECO_DADOS):
        if f.endswith('.parquet'):
            arquivos_parquet.append(os.path.join(ENDERECO_DADOS, f))

    # Cria lista de LazyFrames c/ os dados dos arquivos parquets
    # Gera um plano de execução p/ cada um dos arquivos .parquets scaneados e
    # adiciona-os na lista de lazyframes.
    lazyframes = []
    for arquivo in arquivos_parquet:
        lazyframes.append(pl.scan_parquet(arquivo))

    # Concatena todos os LazyFrames na lista, tornando-os em um único LazyFrame
    df_concatenado = pl.concat(lazyframes)

    # Coleta os dados do plano e salva em um único arquivo Parquet
    df_concatenado.collect().write_parquet(ARQUIVO_FINAL)  

    print(f'Arquivo Parquet único criado em: {ARQUIVO_FINAL}')

    del df_concatenado
    gc.collect()

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')

except ImportError as e:
    print(f'Erro ao criar arquivo Parquet único: {e}')

