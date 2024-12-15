# pip install matplotlib pandas numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # encodings principais: https://docs.python.org/3/library/codecs.html#standard-encodings
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Filtro dos anos de 2022 e 2023
    df_filtrado = df_ocorrencias[df_ocorrencias['ano'].isin([2022, 2023])]

    # Variáveis 'aisp' e 'hom_doloso'
    df_hom_doloso = df_filtrado[['aisp', 'hom_doloso']]

    # Agrupa e soma 'hom_doloso' por 'aisp'
    df_hom_doloso = df_hom_doloso.groupby(
        ['aisp']).sum(['hom_doloso']).reset_index()

    print(df_hom_doloso.head())

    print('Dados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Obtendo os dados
try:
    print('Obtendo informações sobre Homicídio Doloso...')

    # numpy
    array_hom_doloso = np.array(df_hom_doloso['hom_doloso'])

    # média de hom_doloso
    media_hom_doloso = np.mean(array_hom_doloso)

    # mediana de hom_doloso
    mediana_hom_doloso = np.median(array_hom_doloso)

    # distânicia
    distancia = abs((media_hom_doloso-mediana_hom_doloso)/mediana_hom_doloso)

    # Medidas de Tendência Central
    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média de homicídio doloso: {media_hom_doloso}')
    print(f'Mediana de homicidio doloso: {mediana_hom_doloso}')
    print(f'Distância entre média e mediana: {distancia}')

    # Medidas de dispersão
    # Amplitude total
    maximo = np.max(array_hom_doloso)
    minimo = np.min(array_hom_doloso)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)

    # Quartil - Método weibull
    q1 = np.quantile(array_hom_doloso, 0.25, method='weibull')
    q2 = np.quantile(array_hom_doloso, 0.50, method='weibull')
    q3 = np.quantile(array_hom_doloso, 0.75, method='weibull')

    # IQR (Intervalo interquartil)
    iqr = q3 - q1

    # limite superior
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior
    limite_inferior = q1 - (1.5 * iqr)

    # medidas de posição (ou de dispersão)
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

    # filtrar hom_doloso abaixo q1 "limite inferior"
    df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior]

    # filtrar hom_doloso acima de q3 "limite superior"
    df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior]

    print('\nBatalhões com outliers inferiores: ')
    print(30*'-')
    if len(df_hom_doloso_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_hom_doloso_outliers_inferiores.sort_values(
            by='hom_doloso', ascending=True))

    print('\nBatalhões com outliers superiores: ')
    print(30*'-')
    if len(df_hom_doloso_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_hom_doloso_outliers_superiores.sort_values(
            by='hom_doloso', ascending=False))

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de homicídio doloso: {e}')
    exit()


# Medidas de distribuição
try:
    print('Calculando medidas de distribuição...')

    # assimentria Skewness
    assimetria = df_hom_doloso['hom_doloso'].skew()

    # curtpse - Kurtosis
    curtose = df_hom_doloso['hom_doloso'].kurtosis()

    print('\nMedidas de distribuição: ')
    print(30*'-')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')

except Exception as e:
    print(f'Erro ao calcular as medidas de distribuição: {e}')
    exit()

# medidas de dispersão
try:
    print('Calculando medidas de dispersão...')

    # É uma medida para obsersar a dispersão dos dados
    variancia = np.var(array_hom_doloso)

    # distância da variância para a média
    distancia_var_media = variancia/(media_hom_doloso**2)

    # devio padrão é a raiz quadrada da variância
    desvio_padrao = np.std(array_hom_doloso)

    # coeficiente de variação
    # é a magnitude do desvio padrão em realção a média
    coef_variacao = desvio_padrao/media_hom_doloso

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Dist. var x média: {distancia_var_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coef. variação: {coef_variacao}')

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')
    exit()

# visualizar os dados
try:
    print('Visualizando os dados...')

    # matplotlib é uma biblioteca para visualização de dados
    plt.subplots(2, 2, figsize=(16, 7))
    plt.suptitle('Análise de homicídio doloso no RJ')

    # posição 1: bloxplot sem outliers
    plt.subplot(2, 2, 1)
    plt.boxplot(array_hom_doloso, vert=False, showmeans=True, meanline=True)
    plt.title('Boxplot com outliers')

    # posição 2: Ranking das cidades outliers superiores
    plt.subplot(2, 2, 2)

    # ordenar
    if df_hom_doloso_outliers_superiores.empty:
        # Ordenar todos os BPMs em ordem decrescente
        df_hom_doloso_ordered = df_hom_doloso.sort_values(by='hom_doloso', ascending=False)

        # Criar o gráfico de barras com os BPMs ordenados
        plt.bar(df_hom_doloso_ordered['aisp'], df_hom_doloso_ordered['hom_doloso'])
        plt.title('Ranking de homicídios dolosos por BPM')
    else:
        # Ordenar os outliers superiores em ordem decrescente
        df_hom_doloso_outliers_superiores_ordered = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso', ascending=False)

        # Criar o gráfico de barras para os outliers
        plt.bar(df_hom_doloso_outliers_superiores_ordered['aisp'], df_hom_doloso_outliers_superiores_ordered['hom_doloso'], color='red')
        plt.title('Ranking dos batalhõess com outliers superiores')

    # posição 3: Medidas descritivas
    plt.subplot(2, 2, 3)

    # impressão dos valores
    plt.text(0.1, 0.9, f'Média: {media_hom_doloso}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana_hom_doloso}', fontsize=12)
    plt.text(0.1, 0.7, f'Distância: {distancia}', fontsize=12)
    plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12)
    plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
    plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
    plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
    plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)
    
    plt.text(0.7, 0.9, f'Assimetria: {assimetria}', fontsize=12)
    plt.text(0.7, 0.8, f'Curtose: {curtose}', fontsize=12)
    plt.text(0.7, 0.7, f'Variância: {variancia}', fontsize=12)
    plt.text(0.7, 0.6, f'Distância var x média: {distancia_var_media}', fontsize=12)
    plt.text(0.7, 0.5, f'Desvio padrão: {desvio_padrao}', fontsize=12)
    plt.text(0.7, 0.4, f'Coef. variação: {coef_variacao}', fontsize=12)

    # desativar os eixos
    plt.axis('off')

    # ajsutar o layout
    plt.tight_layout()

    # exibir o painel
    plt.show()

except Exception as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()
