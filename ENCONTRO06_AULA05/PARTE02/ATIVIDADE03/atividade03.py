# ATIVIDADE 1
# Treinamento de Análise de Dados
#  Instalar as dependências:
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

    # Somar os estelionatos por mes_ano
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print("Dados obtido com sucesso\n")
    print(df_estelionato.head())

except Exception as e:
    print(f'Erro dados não obtido: {e}')
    exit()


try:
    # print('Obtendo informações...')
    array_estelionato = np.array(df_estelionato['estelionato'])
    array_mes_ano = np.array(df_estelionato['mes_ano'])
    tot_estelionato = np.sum(df_estelionato['estelionato'])
    # Média dos estelionatos
    media_estelionato = np.mean(array_estelionato)
    # Mediana dos esteliontatos
    mediana_estelionato = np.median(array_estelionato)
    # Distância entre a média e a mediana
    distancia_media_mediana = np.abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100

    # Quartis
    q1 = np.quantile(array_estelionato, 0.25)  # Q1 é 25%
    q2 = np.quantile(array_estelionato, 0.50)  # Q2 é 50% (mediana)
    q3 = np.quantile(array_estelionato, 0.75)  # Q3 é 75%

    # Estelionatos abaixo Quartis 1
    df_estelionatos_menores = df_estelionato[df_estelionato['estelionato'] < q1]

    # Estelionatos acima Quartis 3
    df_estelionatos_maiores = df_estelionato[df_estelionato['estelionato'] > q3]


    # Imprime Mes_Anos com Menores ocorrências de Estelionatos (< Quartis 1)
    print('\nMeses e Anos com quantidades menores de estelionatos: ')
    print(30*'-')
    print(df_estelionatos_menores.sort_values(by='estelionato', ascending=True))

    # Imprime Mes_Anos com Maiores ocorrências de Estelionatos (> Quartis 3)
    print('\nMeses e Anos com quantidades maiores de estelionatos: ')
    print(30*'-')
    print(df_estelionatos_maiores.sort_values(by='estelionato', ascending=False))

    # Impressão: Medidas de tendência central
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de estelionatos: {media_estelionato:.3f}')
    print(f'Mediana de estelionatos: {mediana_estelionato}')
    print(f'Distância Média e Medidiana: {distancia_media_mediana:.3f}')

    # Impressão: Medidas de Posição | Dispersão)
    print('\nMedidas de posição: ')
    print(30*'-')
    print(f'Quartis 1: {q1}')
    print(f'Quartis 2: {q2}')
    print(f'Quartis 3: {q3}')

    print('Opinião Fundamentada:')
    print()
    print(30*'-')
    print("Conclusão:")
    print(30*'-')
    print(f"Total de Estelionatos: {tot_estelionato}")
    print(f"\nPara um total de {tot_estelionato} ocorrências de estelionatos, em 25% dos meses")
    print(f" no período de Jan/2003 a Jul/2024, o número de ocorrências foi menor que {q1} ocorrências.")
    print(f"Em contrapartida, em 25% dos meses neste mesmo período, o número de ocorrências superou {q3} casos.")
    print(f"Em compensação, em 75% dos meses, o número de ocorrências foi menor que {q3} casos.")
    
except Exception as e:
    print(f'Erro ao obter informações sobre estelionatos: {e}')
    exit()
