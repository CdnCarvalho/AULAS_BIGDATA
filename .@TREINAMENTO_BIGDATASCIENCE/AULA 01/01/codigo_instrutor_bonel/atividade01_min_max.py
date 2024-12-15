# Instalar as dependências
# pip install pandas
# pip intall numpy

import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    # Importa os dados da web
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Importando somente as colunas: mes_ano e estelionatos
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    # Somar os estelionatos por mes_ano
    df_estelionato = df_estelionato.groupby(
        ['mes_ano']).sum(['estelionato']).reset_index()
    
    print("Dados obtido com sucesso\n")

    print(df_estelionato.head())


except Exception as e:
    print(f'Erro dados não obtido: {e}')
    exit()


try:
    # print('Obtendo informações...')
    array_estelionato = np.array(df_estelionato['estelionato'])
    array_mes_ano = np.array(df_estelionato['mes_ano'])

    # Média dos estelionatos
    media_estelionato = np.mean(array_estelionato)

    # Mediana dos esteliontatos
    mediana_estelionato = np.median(array_estelionato)

    # Maior mes_ano | Maior qtde de estelionato
    max_mes_ano = np.max(array_mes_ano)
    max_estelionato = np.max(array_estelionato)

    # Menor mes_ano | Menor qtde de estelionato
    min_mes_ano = np.min(array_mes_ano)
    min_estelionato = np.min(array_estelionato)

    # Quartis
    q1 = np.quantile(array_estelionato, 0.25)  # Q1 é 25%
    q2 = np.quantile(array_estelionato, 0.50)  # Q2 é 50% (mediana)
    q3 = np.quantile(array_estelionato, 0.75)  # Q3 é 75%

    # Estelionatos abaixo Quartis 1
    df_estelionatos_menores = df_estelionato[df_estelionato['estelionato'] < q1]

    # Estelionatos acima Quartis 3
    df_estelionatos_maiores = df_estelionato[df_estelionato['estelionato'] > q3]

    # Medidas de tendência central
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de estelionatos: {media_estelionato}')
    print(f'Mediana de estelionatos: {mediana_estelionato}')

    # Medidas de Posição | Dispersão)
    print('\nMedidas de posição: ')
    print(30*'-')
    print(f'Quartis 1: {q1}')
    print(f'Quartis 2: {q2}')
    print(f'Quartis 3: {q3}')

    # Imprime Mes_Anos com Menores ocorrências de Estelionatos (< Quartis 1)
    print('\nMeses e Anos com quantidades menores de estelionatos: ')
    print(30*'-')
    print(df_estelionatos_menores.sort_values(
        by='estelionato', ascending=True))

    # Imprime Mes_Anos com Maiores ocorrências de Estelionatos (> Quartis 3)
    print('\nMeses e Anos com quantidades maiores de estelionatos: ')
    print(30*'-')
    print(df_estelionatos_maiores.sort_values(
        by='estelionato', ascending=False))

    # Imprime Mes_Ano c/ Maior qtde de estelionato
    print("\nMês e Ano - Maior Estelionato")
    print(30*'-')
    print("Mes_Ano\t\tEstelionatos")
    print(f"{max_mes_ano}\t\t{max_estelionato}")

    # Imprime Mes_Ano c/ Menor qtde de estelionato
    print("\nMês e Ano - Menor Estelionato")
    print(30*'-')
    print("Mes_Ano\t\tEstelionatos")
    print(f"{min_mes_ano}\t\t{min_estelionato}")

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()
