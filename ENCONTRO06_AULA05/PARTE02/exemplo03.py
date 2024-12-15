# pip install pandas
import pandas as pd
import numpy as np

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por munic
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())
    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# obter informações sobre padrão de roubo_veiculo
try:
    print('Obtendo informações sobre padrão de roubo de veículos...')
    # Arryay numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    # média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    # mediana de roubo_veiculo
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    # Distância entre a média e a mediana
    distancia_media_mediana = np.abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

    # Quartis
    # Método padrão é o weibull 
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull') # Q1 é 25% 
    q2 = np.quantile(array_roubo_veiculo, 0.50, method='weibull') # Q2 é 50% (mediana)
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull') # Q3 é 75%

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo abaixo q1
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]

    # filtrar o dataframe df_roubo_veiculo para o munics com roubo de veículo acima q3
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Distância entre média e mediana: {distancia_media_mediana}')

    print('\nMedidas de posição: ')
    print(30*'-')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    print('\nMunicípios com qtdes menores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

    print('\nMunicípios com qtdes maiores de roubo de veículos: ')
    print(30*'-')
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()