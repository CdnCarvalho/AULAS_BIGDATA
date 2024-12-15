import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # filtrar dados entre 2020 e 2023
    df_filtrados = df_ocorrencias[df_ocorrencias['ano'].isin([2020, 2021, 2022, 2023])]

    # variáveis 'cisp' e 'lesao_corp_dolosa'
    df_lesao_corp = df_filtrados[['cisp', 'lesao_corp_dolosa', 'lesao_corp_culposa']]

    # agrupar por 'cisp' e somar ocorrências
    df_lesao_corp = df_lesao_corp.groupby('cisp').sum().reset_index()

    print(df_lesao_corp.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    print('Obtendo dados das Lesões Corporais')

    # Array Numpy
    array_lesoes_corp_dolosas = np.array(df_lesao_corp['lesao_corp_dolosa'])
    array_cisp = np.array(df_lesao_corp['cisp'])

    # média de lesão corporal dolosa por cisp
    media_lesoes_corp_dolosas = np.mean(array_lesoes_corp_dolosas)
    mediana_lesoes_corp_dolosas = np.median(array_lesoes_corp_dolosas)

    # distancia
    distancia = abs(media_lesoes_corp_dolosas - mediana_lesoes_corp_dolosas) / mediana_lesoes_corp_dolosas

    # IMPRIME MEDIDAS DE TENDÊNCIA CENTRAL
    print('\nMedidas de tendência central')
    print(30 * '=')
    print(f'Média de lesão corporal dolosa: {media_lesoes_corp_dolosas:.3f}')
    print(f'Mediana de lesão corporal dolosa: {mediana_lesoes_corp_dolosas:.3f}')
    print(f'Distância entre média e mediana: {distancia:.3f}')

    # Medida de dispersão Amplitude total
    maximo = np.max(array_lesoes_corp_dolosas)
    minimo = np.min(array_lesoes_corp_dolosas)
    amplitude_total = maximo - minimo

    # IMPRIME MEDIDAS DE DISPERSÃO
    print('\nMedidas de dispersão')
    print(30 * '=')
    print(f'Amplitude total: {amplitude_total:.3f}')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')

    # Amplitude Interquartilica
    q1 = np.percentile(array_lesoes_corp_dolosas, 25)
    q2 = np.percentile(array_lesoes_corp_dolosas, 50)
    q3 = np.percentile(array_lesoes_corp_dolosas, 75)

    # intervalo interquartil
    amplitude_interquartilica = q3 - q1

    # limites para outliers
    limite_inferior = q1 - (1.5 * amplitude_interquartilica)
    limite_superior = q3 + (1.5 * amplitude_interquartilica)

    # IMPRIME MEDIDAS DE POSIÇÃO
    print('\nMedidas de Posição')
    print(30 * '=')
    print(f'Mínimo: {minimo}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Médiana: {q2}')
    print(f'Q3: {q3}')
    print(f'Amplitude Interquartilica: {amplitude_interquartilica}')
    print(f'Limite superior: {limite_superior}')
    print(f'Máximo: {maximo}')

    # imprime os valores que estão fora dos limites
    print('\nValores fora dos limites')
    print(30 * '=')

    # outliers inferiores
    df_lesao_corp_outliers_inferiores = df_lesao_corp[df_lesao_corp['lesao_corp_dolosa'] < limite_inferior]

    # outliers superiores
    df_lesao_corp_outliers_superiores = df_lesao_corp[df_lesao_corp['lesao_corp_dolosa'] > limite_superior]

    # imprime delegacia com outliers inferiores
    print('\nDelegacia com outliers inferiores')
    print(30 * '=')
    if df_lesao_corp_outliers_inferiores.empty:
        print('Não há batalhões com outliers inferiores')
    else:
        print(df_lesao_corp_outliers_inferiores.sort_values(by='lesao_corp_dolosa', ascending=True))

    # imprime delegacias com outliers superiores
    print('\nBatalhão com outliers superiores')
    print(30 * '=')
    if df_lesao_corp_outliers_superiores.empty:
        print('Não há batalhões com outliers superiores')
    else:
        print(df_lesao_corp_outliers_superiores.sort_values(by='lesao_corp_dolosa', ascending=False))

except Exception as e:
    print(f'Erro ao processar dados: {e}')
    exit()

# MEDIDAS DE DISTRIBUIÇÃO (ASSIMETRIA E CURTOSE)
try:
    print('\n\nDistribuição de lesões corporais dolosas')

    # Calcula assimetria e curtose
    assimetria = df_lesao_corp['lesao_corp_dolosa'].skew()
    curtose = df_lesao_corp['lesao_corp_dolosa'].kurtosis()

    print('\nMedidas de Distribuição...')
    print(30 * '=')
    print(f'Assimetria: {assimetria:.3f}')
    print(f'Curtose: {curtose:.3f}')

except Exception as e:
    print(f'Erro ao obter medidas de distribuição: {e}')
    exit()

# MEDIDAS DE DISPERSÃO (Desvio Padrão, Coeficiente de Variação, Variância e Distância da Variância à Média)
try:
    print('\n\nMedidas de Dispersão')

    variancia = np.var(array_lesoes_corp_dolosas)
    distancia_var_media = variancia / (media_lesoes_corp_dolosas ** 2)
    desvio_padrao = np.std(array_lesoes_corp_dolosas)
    coeficiente_variacao = desvio_padrao / media_lesoes_corp_dolosas

    print('\nMedidas de dispersão...')
    print(30 * '=')
    print(f'Variância: {variancia:.3f}')
    print(f'Distância da variância para a média: {distancia_var_media:.3f}')
    print(f'Desvio padrão: {desvio_padrao:.3f}')
    print(f'Coeficiente de variação: {coeficiente_variacao:.3f}')

except Exception as e:
    print(f'Erro ao obter medidas de dispersão: {e}')
    exit()

# VERIFICAR CORRELAÇÃO (LESÕES DOLOSAS X CULPOSAS)
try:
    print('\n\nVerificar correlação entre lesões dolosas e culposas')

    # Calcula correlação entre as variáveis
    correlacao = np.corrcoef(
        df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_culposa'])[0, 1]

    print('\nObtendo correlação...')
    print(30 * '=')
    print(f'Correlação entre lesões dolosas e culposas: {correlacao:.3f}')

except Exception as e:
    print(f'Erro ao obter correlação: {e}')
    exit()

# VISUALIZAÇÃO DOS DADOS
try:
    print('\n\nVISUALIZAÇÃO DOS DADOS')
    print(30 * '=')
    print('Obtendo visualização dos dados...')

    # matplotlib
    plt.subplots(2, 2, figsize=(18, 10))
    plt.suptitle('Análise Lesão Corporal Dolosa e Lesão Corporal Culposa')

    # posição 1: Scatter plot - Correlação entre lesões dolosas e culposas
    plt.subplot(2, 2, 1)
    plt.scatter(df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_culposa'], c='red')
    plt.title('Lesão Corporal Dolosa e Lesão Corporal Culposa')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Lesão Corporal Culposa')

    # posição 2: Boxplot
    plt.subplot(2, 2, 2)
    plt.boxplot(array_lesoes_corp_dolosas, vert=False)
    plt.title('Boxplot - Lesão Corporal Dolosa')
    plt.xlabel('Lesão Corporal Dolosa')

    # posição 3: Histogram
    plt.subplot(2, 2, 3)
    plt.hist(array_lesoes_corp_dolosas, bins=20, color='green', alpha=0.7)
    plt.title('Histograma - Lesão Corporal Dolosa')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Frequência')

    # posição 4: Gráfico de linhas
    plt.subplot(2, 2, 4)
    plt.plot(array_cisp, array_lesoes_corp_dolosas, color='blue')
    plt.title('Evolução das Lesões Corporais Dolosas')
    plt.xlabel('CISP')
    plt.ylabel('Lesão Corporal Dolosa')

    # Ajusta o layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

except Exception as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
