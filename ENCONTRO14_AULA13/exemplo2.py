import polars as pl
from datetime import datetime
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np


ENDERECO_DADOS = r'./dados/'

# Lendo os dados do arquivo Parquet
try:
    print('\nIniciando leitura do arquivo parquet...')

    # Pega o tempo inicial
    inicio = datetime.now()

    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + '/bronze/bolsa_familia.parquet') 

    
    print(df_bolsa_familia.head())

    # Pega o tempo final
    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except Exception as e: 
    print(f'Erro ao ler os dados do parquet: {e}')


# Scan_parquet: Geralment é um método mais rápido que read_parquet,
# pois não carrega os dados em memória imediatamente.
# Gera um plano de execução, para realizar a leitura dos dados.
# Um plano de execução é a melhor rota para realizar a leitura dos dados, 
# utilizando o mínimo de recursos de processamento local (memória e núcleos de processamento)    
# df_bolsa_familia_plan = pl.scan_parquet(ENDERECO_DADOS + '/bronze/bolsa_familia.parquet')    
# df_bolsa_familia = df_bolsa_familia_plan.collect()



# # Visualizar a distribuição dos valores das parcelas em um boxplot
# try:
#     print('Visualizando a distribuição dos valores das parcelas em um boxplot...')

#     # Marcar a hora de início
#     hora_inicio = datetime.now()

#     # Criar um Array Numpy com o valor da parcela
#     array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

#     # criar um boxplot
#     plt.boxplot(array_valor_parcela, vert=False)
#     plt.title('Distribuição dos valores das parcelas')

#     # marcar a hora de término
#     hora_fim = datetime.now()

#     plt.show()

#     print(f'Tempo de execução: {hora_fim - hora_inicio}')
#     print('Dados visualizados com sucesso!')

# except Exception as e:
#     print(f'Erro ao visualizar dados: {e}')