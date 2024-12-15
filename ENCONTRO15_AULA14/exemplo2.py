import polars as pl
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt

ENDERECO_DADOS = r'./dados/'

# LENDO OS DADOS DO ARQUIVO PARQUET
try:
    print('\nIniciando leitura do arquivo parquet...')

    # Pega o tempo inicial
    inicio = datetime.now()

    # Scan_parquet: Cria um plano de execução preguiçoso para a leitura do parquet
    df_bolsa_familia_plan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Executa as operações lazys e coleta os resultados
    df_bolsa_familia = df_bolsa_familia_plan.collect()

    print(df_bolsa_familia)

    # Pega o tempo final
    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except ImportError as e: 
    print(f'Erro ao ler os dados do parquet: {e}')


# Processamento e visualização 
# (12 estados com maior valor de parcela)
try:
    print('Calculando os 12 estados com maior valor de parcelas e gerando gráfico de barras e boxplot...')

    # Agrupar por UF e somar o valor das parcelas
    df_estado_parcelas = df_bolsa_familia.group_by('UF').agg(pl.col('VALOR PARCELA').sum().alias('TOTAL PARCELA'))

    # Ordenar de forma decrescente e pegar os 12 primeiros
    df_estado_parcelas = df_estado_parcelas.sort('TOTAL PARCELA', descending=True).head(12)

    # Exibir o DataFrame resultante
    print(df_estado_parcelas)

    # Criar a figura com dois subgráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gerar gráfico de barras
    ax1.bar(df_estado_parcelas['UF'], df_estado_parcelas['TOTAL PARCELA'])
    ax1.set_xlabel('Estado (UF)', fontsize=12)
    ax1.set_ylabel('Total das Parcelas', fontsize=12)
    ax1.set_title('Top 12 Estados com Maior Total de Parcelas', fontsize=14)
    ax1.set_xticklabels(df_estado_parcelas['UF'], rotation=45, ha='right')

    # Gerar boxplot
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])
    ax2.boxplot(array_valor_parcela, vert=False)
    ax2.set_title('Distribuição dos Valores das Parcelas', fontsize=14)

    # Ajustar layout
    plt.tight_layout()

    # Exibir gráficos
    plt.show()

    print('Gráficos gerados com sucesso!')

except ImportError as e:
    print(f'Erro ao visualizar os dados: {e}')

