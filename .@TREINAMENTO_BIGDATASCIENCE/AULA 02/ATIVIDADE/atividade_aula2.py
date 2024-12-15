'''
Atividade 2

O governador do estado do Rio de Janeiro te chamou em uma reunião e solicitou 
um estudo sobre as recuperações de veículos através das delegacias de polícia.

Ele pontuou que precisa obter as seguintes respostas:

Consigo afirmar que todas as delegacias possuem um padrão médio de recuperação 
de veículos ou isso é meio disperso? Será que existe um padrão predominante ou 
não?

Se não existe padrão, existe alguma (ou algumas) delegacia(s) que foge(m) o 
padrão das recuperações de veículos, ou seja, recuperam muito mais, que as 
demais, a ponto desse nível ser muito discrepante. Se existir, por favor, 
liste-as para mim.

Quais as delegacias com menos de recuperações de veículos?

Utilize os dados de registro de ocorrências do ISP RJ.
'''


import os
import pandas as pd
import numpy as np

os.system('cls')

try:
    print('Obtendo dados...')

    DADOS_ISP = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(
        DADOS_ISP, sep=';', encoding='iso-8859-1'
    )

    df_recuperacao_veiculos = df_ocorrencias[[
        'cisp', 'munic', 'recuperacao_veiculos']]

    df_recuperacao_veiculos = df_recuperacao_veiculos.groupby(
        ['cisp', 'munic']).sum(['recuperacao_veiculos']).reset_index()

    # print(type(df_recuperacao_veiculos))
    print(df_recuperacao_veiculos.head())


except Exception as e:
    print(f'\nErro ao obter dados {e}')
    exit()


# DADOS: (RECUPERAÇÃO DE VEÍCULOS)
try:
    print("\nDados sendo obtido...")

    # NUMPY ARRAY
    array_recuperacao_veiculos = np.array(
        df_recuperacao_veiculos['recuperacao_veiculos'])

    # MEDIDAS DE TENDÊNCIA CENTRAL
    media_recuperacao_veiculo = np.mean(array_recuperacao_veiculos)
    mediana_recuperacao_veiculo = np.median(array_recuperacao_veiculos)
    distancia = abs(media_recuperacao_veiculo -
                    mediana_recuperacao_veiculo) / mediana_recuperacao_veiculo

    # MEDIDAS DE DISPERSÃO
    # 269057
    maximo = np.max(array_recuperacao_veiculos)
    # 24
    minimo = np.min(array_recuperacao_veiculos)
    # 269033
    amplitude_total = maximo - minimo

    # QUARTIS (mtd Weibull)
    q1 = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
    q2 = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
    q3 = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')

    # IQR (INTERVALO INTERQUARTIL)
    iqr = q3 - q1

    # LIMITE SUPERIOR: OUTLIERS SUPERIORES > Q3
    limite_superior = q3 + (1.5 * iqr)

    # LIMITE INFERIOR: OUTLIERS INFERIORES < Q1
    limite_inferior = q1 - (1.5 * iqr)

    # OUTLIERS SUPERIORES
    df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos[
        df_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior]

    # OUTLIERS INFERIORES
    df_recuperacao_veiculos_outliers_inferiores = df_recuperacao_veiculos[
        df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior]

    # DELEGACIAS QUE MENOS RECUPERAM
    df_recuperacao_veiculos_delegacias_recup_menos = df_recuperacao_veiculos[
        df_recuperacao_veiculos['recuperacao_veiculos'] < q1]

    # SAÍDAS: TENDÊNCIA CENTRAL
    print('\nMEDIDAS DE TENDÊNCIA CENTRAL P/ RECUPERAÇÃO DE VEÍCULOS: ')
    print(80*'-')
    print(f'Média: {media_recuperacao_veiculo:.4f}')
    print(f'Mediana: {mediana_recuperacao_veiculo:.4f}')
    print(f'Distância: {distancia:.4f}')

    # SAÍDAS: MEDIDAS DE DISPERSÃO
    print('\nMEDIDAS DE DISPERSÃO P/ RECUPERAÇÃO DE VEÍCULOS: ')
    print(80*'-')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')

    # SAÍDAS: MEDIDAS DE POSIÇÃO OU DISPERSÃO
    print('\nMEDIDAS DE POSIÇÃO: ')
    print(80*'-')
    print('Mínimo: ', minimo)
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Limite Superior: {limite_superior}')
    print('Máximo: ', maximo)

    # SAÍDAS: OUTLIERS INFERIORES
    print('\nDELEGACIAS COM OUTLIERS INFERIORES: ')
    print(80*'-')
    if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
        print('Não existem outliers inferiores')
    else:
        print(df_recuperacao_veiculos_outliers_inferiores.sort_values(
            by='recuperacao_veiculos', ascending=True))

    # SAÍDAS: OUTLIERS SUPERIORES (DELEGACIAS QUE RECUPERAM MUITO ALÉM)
    print(
        '\nDELEGACIAS QUE MAIS RECUPERAM (DADOS DISCREPANTES - OUTLIERS '
        'SUPERIORES:)')
    print(80*'-')
    if len(df_recuperacao_veiculos_outliers_superiores) == 0:
        print("Não existem outilers superiores")
    else:
        print(df_recuperacao_veiculos_outliers_superiores.sort_values(
            by='recuperacao_veiculos', ascending=False))

    # SAÍDAS: DELEGACIAS QUE MENOS RECUPERAM
    print("\nAS 25% DAS DELEGACIAS QUE MENOS RECUPERAM VEÍCULOS")
    print(80*'-')
    print(df_recuperacao_veiculos_delegacias_recup_menos.sort_values(
        by='recuperacao_veiculos', ascending=True))

    # ///////// SAÍDAS: RESPOSTA AOS QUESTIONAMENTOS: ///////////////
    print("\nRESPOSTA AO GOVERNADOR: ")
    print(80*'-')
    print('MEDIDAS DE TENDÊNCIA CENTRAL :')
    print(f'Com Média {media_recuperacao_veiculo:.4f} e Mediana '
          f'{mediana_recuperacao_veiculo}, a distribuição dos dados é '
          f'assimétrica em torno de {(distancia * 100):.2f}%. Bem acima dos '
          '25%. Neste caso, não temos um padrão.')

    print('\nMEDIDAS DE PODIÇÃO E DISPERSÃO:')
    print(f'Os dados são dispersos, a Amplitude total {amplitude_total} está '
          f'próxima ao máximo {maximo}. Mostra a heterogeidade dos dados, '
          'que tendem a ter outliers.')

    print('\nANÁLISE DOS QUARTIS:')
    print(f'O Intervalo Interquartil {iqr}, que é a amplitude do intervalo '
          'dados centrais, está bem próximo ao valor de Q3 {q3}. '
          'Mostra que os dados são heterogênios.')


except Exception as e:
    print(f"\nErro ao obter dados {e}")
    exit()
