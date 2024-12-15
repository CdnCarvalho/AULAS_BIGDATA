import pandas as pd
import numpy as np

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Demilitando somente as variáveis munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Somando roubo_veiculo por município
    df_roubo_veiculo = df_roubo_veiculo.groupby(
        ['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())
    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Obter informações sobre padrão de roubo_veiculo
try:
    # Array numpy é uma estrutura de dados que armazena uma coleção de dados
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    
    # Calcula a média de roubo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    # Calcula mediana de roubo
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    # Distânicia
    distancia = abs(
        (media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo
    )

    # Medidas de tendência central
    # Se a média for próxima dos (25%) da mediana, ainda pode ser, que haja um padrão
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia}')

    # Medidas de dispersão
    # Amplitude total: Quanto mais próximo de zero, maior a
    # homogeinidade dos dados
    # Se for igual a zero, todos os valores são iguais
    # Quanto mais próximo do máximo, maior a dispersão 
    # dos dados ou a heterogeneidade
    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)

    # Quartis - Uso método weibull
    q1 = np.quantile(
        array_roubo_veiculo, 0.25, method='weibull')  # 25%
    q2 = np.quantile(
        array_roubo_veiculo, 0.50, method='weibull')  # 50%
    q3 = np.quantile(
        array_roubo_veiculo, 0.75, method='weibull')  # 75%

    # IQR (Intervalo interquartil) 
    # q3 - q1
    # É a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. 
    # Máximo e Mínimo estão fora do IQR
    # Não sofre a interferência dos valores extremos
    # Quanto mais próximo de zero, mais homogêneo são os dados
    # Quanto mais próximo do q3, mais heterogêneo são os dados
    iqr = q3 - q1

    # limite superior
    # vai identificar os outliers acima de q3
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior
    # vai identificar os outliers abaixo de q1
    limite_inferior = q1 - (1.5 * iqr)

    # Medidas de Posição (ou de Dispersão)
    print('\nMedidas de posição: ')
    print(30*'-')
    print('Mínimo: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Máximo: ', maximo)

    # Filtrar o dataframe df_roubo_veiculo para os municípios 
    # com outliers inferiores (valores discrepantes)
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para os municípios 
    # com outliers superiores (valores discrepantes)
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[
        df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    # Printando municípios com outliers Inferiores
    print('\nMunicípios com outliers inferiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(
            by='roubo_veiculo', ascending=True))

    print('\nMunicípios com outliers superiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(
            by='roubo_veiculo', ascending=False))

except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()
