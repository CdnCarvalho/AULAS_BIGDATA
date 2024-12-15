# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
# pip install numpy
# pip install pandas
import pandas as pd
import numpy as np

# Obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Encodings: utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Demilitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Totalizar roubo_veiculo por munic
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())

    print('\nDados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Gerando informações...
try:
    print('\nCalculando informações sobre padrão de roubo de veículos...')
    # Array Numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    # Média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    # Mediana de roubo_veiculo - Divide a distribuição em duas partes iguais
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # Média muito diferente da mediana (25% ou mais), distribuição assimétrica. Não tende a haver um padrão
    distancia_media_mediana = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)
 
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de roubo de veículos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veículos: {mediana_roubo_veiculo}')
    print(f'Diferença entre média e mediana: {distancia_media_mediana}%')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()
