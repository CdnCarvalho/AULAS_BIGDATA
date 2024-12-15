import pandas as pd
import numpy as np


# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por município
    df_roubo_veiculo = df_roubo_veiculo.groupby(
        ['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# obter informações sobre padrão de roubo_veiculo
try:
    print('Obtendo informações sobre padrão de roubo de veículos...')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # MÉDIA de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # MEDIANA de roubo_veiculo
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # DISTÂNCIA
    # Para o percentual, ainda multiplicar por 100 o cálculo abaixo
    distancia = abs(
        media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo

    # MEDIDAS DE TENDÊNCIA CENTRAL
    # Se a média for muito diferente da mediana, distribuição é assimétrica. Não tende a haver um padrão
    # e pode ser que existam outliers (valores discrepantes)
    # Se a média for próxima (25%) a mediana, distribuição é simétrica. Tende a haver um padrão
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia}')

    # MEDIDAS DE DISPERSÃO
    # Amplitude total = Maior valor - menor valor
    # Quanto mais próximo de zero, maior a homogeinidade dos dados
    # Se for igual a zero, todos os valores são iguais
    # Quanto mais próximo do máximo, maior a dispersão dos dados ou 
    # heterogeneidade.
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    # print('\nMedidas de dispersão: ')
    # print(30*'-')
    # print('Máximo: ', maximo)
    # print('Mínimo: ', minimo)
    # print('Amplitude total: ', amplitude)

    # Quartis
    # Método padrão é o weibull
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')

    # IQR (Intervalo interquartil)
    # q3 - q1
    # é a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Max e min estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # quanto mais próximo de zero, mais homogêneo são os dados
    # Quanto mais próximo do q3, mais heterogêneo são os dados
    # Não é a melhor medida para analisar variabilidade
    iqr = q3 - q1

    # limite superior
    # vai identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior
    # vai identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)

    # medidas de posição (ou de dispersão)
    print('\nMEDIDAS DE POSIÇÃO: ')
    print(30*'-')
    print('Mínimo: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Máximo: ', maximo)

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo 
    # abaixo q1
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo 
    # acima q3
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    print('\nMUNICÍPIOS COM OUTLIERS INFERIORES: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(
            by='roubo_veiculo', ascending=True))

    print('\nMUNICÍPIOS COM OUTLIERS SUPERIORES: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print("Não existem outilers superiores")
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(
            by='roubo_veiculo', ascending=False))


except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()

