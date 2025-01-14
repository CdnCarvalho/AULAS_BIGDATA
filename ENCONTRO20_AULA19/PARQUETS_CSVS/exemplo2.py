import polars as pl
import os
from datetime import datetime

# Endereço dos dados e arquivo Parquet
ENDERECO_DADOS = r'./dados/'
# ENDERECO_DADOS_NOVOS = r'./dados_novos/'
ARQUIVO_PARQUET = ENDERECO_DADOS + 'bolsa_familia.parquet'

# Obter lista de novos arquivos CSV
novos_csvs = [arquivo for arquivo in os.listdir(ENDERECO_DADOS) if arquivo.endswith('.csv')]

# lista_novos_csvs = []
# lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
# for arquivo in lista_dir_arquivos:
#     if arquivo.endswith('.csv'):
#         lista_novos_csvs.append(arquivo)

try:
    print('Iniciando atualização do arquivo Parquet...')
    inicio = datetime.now()

    # Verificar se o arquivo Parquet já existe
    if os.path.exists(ARQUIVO_PARQUET):
        print('Carregando dados existentes do arquivo Parquet...')
        df_bolsa_familia = pl.scan_parquet(ARQUIVO_PARQUET)  # Leitura preguiçosa
    else:
        print('Arquivo Parquet não encontrado. Criando um novo...')
        df_bolsa_familia = None

    # Processar todos os novos arquivos CSV
    for novo_csv in novos_csvs:
        print(f'Carregando novos dados do arquivo: {novo_csv}')
        df_novo = pl.read_csv(
            ENDERECO_DADOS + novo_csv,
            separator=';',
            encoding='iso-8859-1'
        )

        # Converter a coluna 'VALOR PARCELA' para float
        df_novo = df_novo.with_columns(
            pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
        )

        # Concatenar os novos dados ao DataFrame existente
        if df_bolsa_familia is None:
            print('Entrei no primeiro if')
            df_bolsa_familia = df_novo.lazy()
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df_novo.lazy()])

    # Salvar o DataFrame atualizado como Parquet
    print('Salvando dados atualizados no arquivo Parquet...')
    df_bolsa_familia.collect().write_parquet(ARQUIVO_PARQUET)

    fim = datetime.now()
    print(f'Atualização concluída! Tempo de execução: {fim - inicio}')

except Exception as e:
    print(f'Erro durante a atualização: {e}')
