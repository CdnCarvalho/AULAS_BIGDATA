import pandas as pd
import numpy as np

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Selecionando somente as variáveis:
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    # Totalizar mes_ano por município
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head())
    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    array_estelionato = np.array(df_estelionato['estelionato']) # array numpy
    # media e mediana
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)

    # Distância entre media e mediana | 
    # Até 10% considera que a distribuição tende a uma simetria
    # Entre 10% e 25%, considera que a distribuição tende uma assimentria moderada,
    # simetria moderada
    distancia = abs((media - mediana) / mediana)

    # Quartis
    # há métodos diferntes: 
    # weibull, linear, lower, higher, nearest, midpoint
    q1 = np.quantile(array_estelionato, 0.25, method='weibull')
    q2 = np.quantile(array_estelionato, 0.50, method='weibull')
    q3 = np.quantile(array_estelionato, 0.75, method='weibull')

    # Pegando os meses de maiores ocorrências de estelionatos
    df_mes_ano_acima_q3 = df_estelionato[df_estelionato['estelionato'] > q3]
    # Pegando os meses de menores ocorrências de estelionatos
    df_mes_ano_abaixo_q1 = df_estelionato[df_estelionato['estelionato'] < q1]

    # PRINTS: Saídas na Tela
    print('\nMEIDAS DE TENDÊNCIA CENTRAL: ')
    print(30*'-')
    print('Média: ', media)
    print('Mediana: ', mediana)
    print('Distância: ', distancia)

    print('\nMEDIDAS DE POSIÇÃO: ')
    print(30*'-')
    print('Q1 (25%): ', q1)
    print('Q2 (50%): ', q2)
    print('Q3 (75%): ', q3)

    print('\nMAIORES MESES E ANOS:')
    print(30*'-')
    print(df_mes_ano_acima_q3.sort_values(by='estelionato',ascending=False))

    print('\nMENORES MESES E ANOS:')
    print(30*'-')
    print(df_mes_ano_abaixo_q1.sort_values(by='estelionato'))

except ImportError as e:
    print(f'Erro ao obter maiores e menores: {e}')
    exit()
