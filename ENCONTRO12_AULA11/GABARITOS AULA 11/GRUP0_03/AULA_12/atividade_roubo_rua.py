import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# obter dados
try:
    print('Obtendo dados...')
    # ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    # # utf-8, iso-8859-1, latin1, cp1252
    # df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

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
    df_roubo_rua = pd.read_sql('basedp_roubo_rua', engine)
    # print(df_base.head())
    # print(df_roubo_rua.head())
    print('Dados obtidos com sucesso!')
except ImportError as e:
    print('Erro na conexão do banco de dados', e)


# Preparando os dados   
try:
    # Limpar nomes das colunas para ambos os DataFrames, caso necessário.
    df_base.columns = [col.strip().replace('\ufeff', '') for col in df_base.columns]
    df_roubo_rua.columns = [col.strip().replace('\ufeff', '') for col in df_roubo_rua.columns]

    # Relacionando os dataframes
    df_ocorrencias = pd.merge(df_base, df_roubo_rua, on='cod_ocorrencia')
    print(df_ocorrencias.head())

    # filtrar os anos significa que haverá uma quebra de linha
    df_ocorrencias = df_ocorrencias[(df_ocorrencias['ano'] >= 2022) & (df_ocorrencias['ano'] <= 2023)]
    # print(df_ocorrencias.columns)

    # Demilitando somente as variáveis
    df_roubo_rua = df_ocorrencias[['aisp', 'roubo_rua']]

    # Totalizar
    df_total_roubo_rua = df_roubo_rua.groupby(['aisp']).sum(['roubo_rua']).reset_index()

    # print(df_total_roubo_rua.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# Obtendo medidas que suportarão as análises
try:
    print('Obtendo medidas...')
    # array de Roubos em ruas
    array_roubo_rua = np.array(df_total_roubo_rua['roubo_rua'])

    # medidas de tendência central
    media = np.mean(array_roubo_rua)
    mediana = np.median(array_roubo_rua)
    distancia_media_mediana = (media-mediana)/mediana

    # Medidas de posição
    # Interfere nos outliers
    q1 = np.quantile(array_roubo_rua, 0.25)
    q3 = np.quantile(array_roubo_rua, 0.75)
    q1 = np.quantile(array_roubo_rua, 0.25, method='weibull')
    q3 = np.quantile(array_roubo_rua, 0.75, method='weibull')
    iqr = q3 - q1
    limite_superior = q3 + (1.5 * iqr)

    # Amplitude
    minimo = np.min(array_roubo_rua)
    maximo = np.max(array_roubo_rua)
    amplitude_total = maximo - minimo

    # Medidas de dispersão
    variancia = np.var(array_roubo_rua)
    distancia_media_variancia = variancia / (media ** 2)
    # É a mesma coisa que utilizar o método std => desvio_padrao = np.sqrt(variancia)
    desvio_padrao = np.std(array_roubo_rua)
    coeficiente_variacao = desvio_padrao / media

    # assimetria
    assimentria = df_total_roubo_rua['roubo_rua'].skew()

    # curtose
    curtose = df_total_roubo_rua['roubo_rua'].kurtosis()

    # Identificar os Outliers Superiores
    df_roubo_rua_outliers = df_total_roubo_rua[df_total_roubo_rua['roubo_rua'] > limite_superior]

    # Visualizando os Outliers no Terminal
    print('\nAISPs com Roubos em ruas superiores as demais:')
    print(30*'-')
    if len(df_roubo_rua_outliers) == 0:
        print('Nenhum outlier encontrado.')
        df_total_roubo_rua_final = df_total_roubo_rua.copy()
    else:
        df_total_roubo_rua_final = df_roubo_rua_outliers.copy()

    print(df_total_roubo_rua_final.sort_values(by='roubo_rua', ascending=False))

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

    print('\nOutliers')
    print(30*'-')
    print(df_roubo_rua_outliers)

except Exception as e:
    print(f'Erro ao obter medidas: {e}')
    exit()


# Exibir em um painel
try:
    print('Visualizando dados...')

    plt.subplots(2, 2, figsize=(16, 6))
    plt.suptitle('Análise de Roubos em ruas por AISP', fontsize=18)

    # posição 2: Ranking de Roubos em ruas
    plt.subplot(2, 2, 1)
    # Converter aisp para string

    plt.boxplot(array_roubo_rua, vert=False, showmeans=True, meanline=True)
    plt.title('Roubos em ruas AISP')


    # posição 2: Ranking de Roubos em ruas
    plt.subplot(2, 2, 2)
    # Converter aisp para string
    df_total_roubo_rua_final['aisp'] = df_total_roubo_rua_final['aisp'].astype(str)
    
    if len(df_roubo_rua_outliers) <= 1:
        # Ordenar o dataframe
        df_total_roubo_rua = df_total_roubo_rua.sort_values(by='roubo_rua', ascending=True)
        # Selecionar as 15 primeiras AISPs (ranking dos maiores valores)
        df_top = df_total_roubo_rua[df_total_roubo_rua['roubo_rua'] >= q3]
        # plotar o gráfico
        plt.barh(df_top['aisp'], df_top['roubo_rua'])
        plt.xlabel('Roubos em ruas')
        plt.ylabel('BPMs')
        plt.title('Roubos em ruas por AISP')
    else:
        # Ordenar o dataframe
        df_total_roubo_rua_final = df_total_roubo_rua_final.sort_values(by='roubo_rua', ascending=True)
        # plotar o gráfico
        plt.barh(df_total_roubo_rua_final['aisp'], df_total_roubo_rua_final['roubo_rua'])
        plt.xlabel('Roubos em ruas')
        plt.ylabel('BPMs')
        plt.title('Roubos em ruas por AISP')

    # posição 3: histograma
    plt.subplot(2, 2, 3)
    plt.hist(array_roubo_rua, bins=200, color='blue', edgecolor='black')
    plt.axvline(media, color='red', linewidth=1)
    plt.title('Histograma de Roubos em ruas por AISP')

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

    plt.text(0.7, 1.0, f'Menor Valor: {minimo}', fontsize=12)
    plt.text(0.7, 0.9, f'Maior Valor: {maximo}', fontsize=12)
    plt.text(0.7, 0.8, f'Q1: {q1}', fontsize=12)
    plt.text(0.7, 0.7, f'Q3: {q3}', fontsize=12)
    plt.text(0.7, 0.6, f'IQR: {iqr}', fontsize=12)

    plt.axis('off')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
