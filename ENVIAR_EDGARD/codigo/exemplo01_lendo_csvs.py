import polars as pl
from datetime import datetime
import os

# Dados baixado do link: 2 CSVs
# https://portaldatransparencia.gov.br/download-de-dados/auxilio-emergencial
# arquivo 202004_AuxilioEmergencial.csv - 7.8 GB
# arquivo 202005_AuxilioEmergencial.csv - 9,36 GB

# tempo Tempo de execução: 0:05:46.150817
ENDERECO_DADOS = './dados/'

# Tamanho do bloco de linhas a serem lidas
# Isso pode variar de acordo com a memória disponível
# Você pode escalar este valor de acordo com a sua necessidade
QTD_LINHAS = 10_000_000

# variável para ordenar os parquets
contador_parquet = 0

# Obtendo os dados dos CSVs e gerando parquets divididos
try:
    print('Obtendo dados')

    inicio = datetime.now()

    # Cria uma lista de arquivos .csvs q vem do diretório
    lista_arquivos = []
    for f in os.listdir(ENDERECO_DADOS):
        if f.endswith('.csv'):
            lista_arquivos.append(f)

    # Processa cada arquivo CSV na lista recebida do diretório
    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')
        caminho_csv = os.path.join(ENDERECO_DADOS, arquivo)

        # Streaming de leitura e processamento - Plano de execução
        scan = pl.scan_csv(
            caminho_csv,
            separator=';',
            # Ajuste para lidar com caracteres inválidos
            encoding='utf8-lossy'
        )

        # Coleta o plano de execução
        df = scan.collect()

        # Divide a leitura dos dados em gaps "pedaços" e salva-os em parquet
        for i in range(0, len(df), QTD_LINHAS):
            pedaco = df[i: (i + QTD_LINHAS)]

            # Concatena o caminho e gera o nome do aquivo parquet, numerando-os a cada iteração
            caminho_parquet = os.path.join(
                ENDERECO_DADOS, f'auxilio_emergencial_parte_{contador_parquet}.parquet'
            )

            # Salva os dados em aquivo parquet, numerando-os a cada iteração
            pedaco.write_parquet(caminho_parquet)

            print(f'Parquet parte {contador_parquet} salvo: {caminho_parquet}')

            contador_parquet += 1
        
        del df

    fim = datetime.now()
    print(f'Tempo de execução: {fim - inicio}')

except ImportError as e:
    print(f'Erro ao processar os dados: {e}')
