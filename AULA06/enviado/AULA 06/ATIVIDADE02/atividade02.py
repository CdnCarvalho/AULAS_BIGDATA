# ATIVIDADE 1
# Treinamento de Análise de Dados
# Instalar as dependências:
# pip install pandas
# pip intall numpy

import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # Importa os dados da web
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Importando somente as colunas: mes_ano e estelionatos
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    # Agrupa e soma os estelionatos por mes_ano
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print("Dados obtido com sucesso\n")
    print(df_estelionato.head())

except Exception as e:
    print(f'Erro dados não obtido: {e}')
    exit()


try:
    # print('Obtendo informações...')
    array_estelionato = np.array(df_estelionato['estelionato'])

    # Soma todos os estelionatos
    tot_estelionato = np.sum(df_estelionato['estelionato'])
    # Média dos estelionatos
    media_estelionato = np.mean(array_estelionato)
    # Mediana dos esteliontatos
    mediana_estelionato = np.median(array_estelionato)

    # Calcula a distância entre a média e a mediana
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100
    
    # Impressão dos resultados
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Total geral de estelionatos: {tot_estelionato}')
    print(f'Média de estelionatos: {media_estelionato:.3f}')
    print(f'Mediana de estelionatos: {mediana_estelionato}')
    print(f'Distância entre a média e a mediana: {distancia_media_mediana:.3f}%')


except Exception as e:
    print(f'Erro ao obter informações sobre estelionatos: {e}')
    exit()
