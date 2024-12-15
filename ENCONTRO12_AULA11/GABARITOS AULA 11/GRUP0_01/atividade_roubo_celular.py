import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# obter dados
try:
    print('Obtendo dados...')
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    # Obtendo as variáveis de ambiente
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    df_base = pd.read_sql('basedp', engine)
    df_roubo_celular = pd.read_sql('basedp_roubo_celular', engine)
    # print(df_base.head())
    # print(df_roubo_celular.head())
except ImportError as e:
    print('Erro na conexão do banco de dados', e)

# Preparando os dados   
try:
    df_ocorrencias = pd.merge(df_base, df_roubo_celular, on='cod')
    # print(df_ocorrencias.head())

    # filtrar os anos
    df_ocorrencias = df_ocorrencias[(df_ocorrencias['ano'] >= 2022) & (df_ocorrencias['ano'] <= 2023)]
    # print(df_ocorrencias.columns)

    # Demilitando somente as variáveis a serem utilizadas
    df_roubo_celular = df_ocorrencias[['aisp', 'roubo_celular']]

    # Totalizando os roubos de celular por aisp
    df_total_roubo_celular = df_roubo_celular.groupby(['aisp']).sum(['roubo_celular']).reset_index()

    print(df_total_roubo_celular.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# Obtendo medidas que suportarão as análises
try:
    print('Obtendo medidas...')
    # array de Roubo de Celular
    array_roubo_celular = np.array(df_total_roubo_celular['roubo_celular'])
    # medidas de tendência central
    media = np.mean(array_roubo_celular)
    mediana = np.median(array_roubo_celular)
    distancia_media_mediana = (media-mediana)/mediana

    # Medidas de posição
    q1 = np.quantile(array_roubo_celular, 0.25, method='weibull')
    q3 = np.quantile(array_roubo_celular, 0.75, method='weibull')
    iqr = q3 - q1
    limite_superior = q3 + (1.5 * iqr)

    # Amplitude
    minimo = np.min(array_roubo_celular)
    maximo = np.max(array_roubo_celular)
    amplitude_total = maximo - minimo

    # Medidas de dispersão
    variancia = np.var(array_roubo_celular)
    distancia_media_variancia = variancia / (media ** 2)
    # É a mesma coisa que utilizar o método std => desvio_padrao = np.sqrt(variancia)
    desvio_padrao = np.std(array_roubo_celular)
    coeficiente_variacao = desvio_padrao / media

    # assimetria
    assimentria = df_total_roubo_celular['roubo_celular'].skew()
    # curtose
    curtose = df_total_roubo_celular['roubo_celular'].kurtosis()

    # Identificar os Outliers Superiores
    df_roubo_celular_outliers = df_total_roubo_celular[df_total_roubo_celular['roubo_celular'] > limite_superior]

    # Visualizando os Outliers no Terminal
    print('\nAISPs com Roubos de Celulares superiores as demais:')
    print(30*'-')
    if len(df_roubo_celular_outliers) == 0:
        print('Nenhum outlier encontrado.')
        df_total_roubo_celular_final = df_total_roubo_celular.copy()
    else:
        df_total_roubo_celular_final = df_roubo_celular_outliers.copy()

    print(df_total_roubo_celular_final.sort_values(by='roubo_celular', ascending=False))

    # Exibindo no Terminal
    print('\nMedidas de assimetria e curtose:')
    print(30*'-')
    print(f'Assimetria: {assimentria}')
    print(f'Curtose: {curtose}')

    print('\nMedidas de tendência central:')
    print(30*'-')
    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Distância média x mediana: {distancia_media_mediana}')

    print('\nMedidas de dispersão:')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Distância média x variância: {distancia_media_variancia}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coeficiente de variação: {coeficiente_variacao}')
    print(f'Amplitude total: {amplitude_total}')

    print('\nMedidas de posição:')
    print(30*'-')
    print(f'Menor valor: {minimo}')
    print(f'Q1: {q1}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print(f'Maior valor: {maximo}')

except Exception as e:
    print(f'Erro ao obter medidas: {e}')
    exit()


# Exibir em um painel
try:
    print('Visualizando dados...')

    plt.subplots(2, 2, figsize=(16, 6))
    plt.suptitle('Análise de Roubo de Celular por AISP', fontsize=18)

    # posição 1: Ranking de Roubo de Celular
    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_celular, vert=False, showmeans=True, meanline=True)
    plt.title('Roubo de Celular AISP')

    # posição 2: Ranking de Roubo de Celular
    plt.subplot(2, 2, 2)
    # Converter aisp para string o dataframe final e o dataframe 
    df_total_roubo_celular_final['aisp'] = df_total_roubo_celular_final['aisp'].astype(str)
    df_total_roubo_celular['aisp'] = df_total_roubo_celular['aisp'].astype(str)
    # Ordenar o dataframe
    if len(df_roubo_celular_outliers) <= 1:
        # Ordenar o dataframe
        df_total_roubo_celular = df_total_roubo_celular.sort_values(by='roubo_celular', ascending=True)
        # Selecionar os batalhões com mais roubos (ranking entre os maiores valores)
        df_top = df_total_roubo_celular[df_total_roubo_celular['roubo_celular'] >= q3]
        # plotar o gráfico
        plt.barh(df_top['aisp'], df_top['roubo_celular'])
        plt.xlabel('Roubos em celular')
        plt.ylabel('BPMs')
        plt.title('Roubos em celular por AISP')
    else:
        # Ordenar o dataframe
        df_total_roubo_celular_final = df_total_roubo_celular_final.sort_values(by='roubo_celular', ascending=True)
        # plotar o gráfico
        plt.barh(df_total_roubo_celular_final['aisp'], df_total_roubo_celular_final['roubo_celular'])
        plt.xlabel('Roubos em celular')
        plt.ylabel('BPMs')
        plt.title('Roubos em celular por AISP')

    # posição 3: histograma
    plt.subplot(2, 2, 3)
    plt.hist(array_roubo_celular, bins=200, color='blue', edgecolor='black')
    plt.axvline(media, color='red', linewidth=1)
    plt.title('Histograma de Roubo de Celular por AISP')

    # posição 4: medidas
    plt.subplot(2, 2, 4)
    plt.text(0.1, 1.0, f'Assimetria: {assimentria}', fontsize=12)
    plt.text(0.1, 0.9, f'Curtose: {curtose}', fontsize=12)
    plt.text(0.1, 0.8, f'Média: {media}', fontsize=12)
    plt.text(0.1, 0.7, f'Mediana(Q2): {mediana}', fontsize=12)
    plt.text(0.1, 0.6, f'Dist. média x mediana: {distancia_media_mediana}', fontsize=12)
    plt.text(0.1, 0.5, f'Variância: {variancia}', fontsize=12)
    plt.text(0.1, 0.4, f'Dist. média x variância: {distancia_media_variancia}', fontsize=12)
    plt.text(0.1, 0.3, f'Desvio padrão: {desvio_padrao}', fontsize=12)
    plt.text(0.1, 0.2, f'Coeficiente de variação: {coeficiente_variacao}', fontsize=12)
    plt.text(0.1, 0.1, f'Amplitude total: {amplitude_total}', fontsize=12)

    plt.axis('off')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
