import pandas as pd
import numpy as np


# Obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Selecionando somente as variáveis de municípios e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por município
    df_roubo_veiculo = df_roubo_veiculo.groupby(
        ['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Obter informações sobre Padrão de roubo_veiculo
try:
    print('Obtendo informações sobre padrão de roubo de veículos...')

    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    # MÉDIA (roubo_veiculo)
    media_roubo_veiculo = np.mean(array_roubo_veiculo)

    # MEDIANA (roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # DISTÂNCIA - (Multiplicar por 100, para obter o percentual)
    distancia = abs(
        media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo

    # MEDIDAS DE TENDÊNCIA CENTRAL
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia}')

    # MEDIDAS DE DISPERSÃO
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)

    # QUARTIS (Método padrão é o WEIBULL)
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')

    # IQR (INTERVALO INTERQUARTIL)
    iqr = q3 - q1

    # LIMITE SUPERIOR: Identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # LIMITE INFERIOR: Identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)

    # MEDIDAS DE POSIÇÃO OU DISPERSÃO
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

    # filtrar o dataframe df_roubo_veiculo para o municípios
    # com roubo de veículo abaixo q1
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para o municípios 
    # com roubo de veículo acima q3
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
