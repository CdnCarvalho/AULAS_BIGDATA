import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # filtrar dados entre 2020 e 2023
    df_filtrados = df_ocorrencias[(
        df_ocorrencias['ano'].isin([2020, 2021, 2022, 2023]))]

    # variáveis 'cisp' e 'lesao_corp_dolosa'
    df_lesao_corp = df_filtrados[[
        'cisp', 'lesao_corp_dolosa', 'lesao_corp_culposa']]
    # print(df_lesao_corp)
    
    # agrupar por 'cisp' e somar ocorrências
    df_lesao_corp = df_lesao_corp.groupby(
        'cisp').sum(['df_lesao_corp']).reset_index()

    print(df_lesao_corp.head())

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


try:
    # arrays para armazenar os dados - numpy
    print('Obtendo dados das Lesões Corporais')

    # Array Numpy
    array_lesoes_corp_dolosas = np.array(df_lesao_corp['lesao_corp_dolosa'])
    array_cisp = np.array(df_lesao_corp['cisp'])
    # print(array_cisp)

    # média de lesão corporal dolosa por cisp
    media_lesoes_corp_dolosas = np.mean(array_lesoes_corp_dolosas)

    # mediana_lesoes_corp_dolosas = np.median(array_lesoes_corp_dolosas)
    mediana_lesoes_corp_dolosas = np.median(array_lesoes_corp_dolosas)

    # distancia
    distancia = abs((
        media_lesoes_corp_dolosas - mediana_lesoes_corp_dolosas)) / mediana_lesoes_corp_dolosas

    # IMPRIME MEDIDAS DE TENDENCIA CENTRAL
    print('\nMedidas de tendência central')
    print(30*'=')
    print(f'Média de lesão corporal dolosa: {media_lesoes_corp_dolosas:.3f}')
    print(f'Mediana de lesão corporal dolosa: {mediana_lesoes_corp_dolosas:.3f}')
    print(f'Distância entre média e mediana: {distancia:.3f}')

    # Medida de dispersão Amplitude total
    maximo = np.max(array_lesoes_corp_dolosas)
    minimo = np.min(array_lesoes_corp_dolosas)
    amplitude_total = maximo - minimo

    # IMPRIME MEDIDAS DE DISPERSÃO
    print('\nMedidas de dispersão')
    print(30*'=')
    print(f'Amplitude total: {amplitude_total:.3f}')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')

    # Amplitude Interquartilica
    q1 = np.percentile(array_lesoes_corp_dolosas, 25)
    q2 = np.percentile(array_lesoes_corp_dolosas, 50)
    q3 = np.percentile(array_lesoes_corp_dolosas, 75)

    # Intervalo Interquartil
    amplitude_interquartilica = q3 - q1

    # Limite Inferior - Limite Outliers Inferiores
    limite_inferior = q1 - (1.5 * amplitude_interquartilica)

    # Limite Superior - Limite Outliers Superiores
    limite_superior = q3 + (1.5 * amplitude_interquartilica)

    # IMPRIME MEDIDAS DE POSIÇÃO
    print('\nMedidas de Posição')
    print(30*'=')
    print(f'Mínimo: {minimo}')
    print(f'Limite inferior: {limite_inferior}')
    print(f'Q1: {q1}')
    print(f'Médiana: {q2}')
    print(f'Q3: {q3}')
    print(f'Amplitude Interquartilica: {amplitude_interquartilica}')
    print(f'Limite superior: {limite_superior}')
    print(f'Máximo: {maximo}')

    # Imprime os valores que estão fora dos limites
    print('\nValores fora dos limites')
    print(30*'=')

    # Outliers inferiores # Filtrar lesao_corporal_dolosa abaixo 'limite inferior'
    df_lesao_corp_outliers_inferiores = df_lesao_corp[
        df_lesao_corp['lesao_corp_dolosa'] < limite_inferior]
    # print(df_lesao_corp_outliers_inferiores)

    # Outliers superiores # Filtrar lesao_corporal_dolosa acima Q3
    df_lesao_corp_outliers_superiores = df_lesao_corp[
        df_lesao_corp['lesao_corp_dolosa'] > limite_superior]
    # print(df_lesao_corp_outliers_superiores)

    # Imprime delegacia com outliers inferiores
    print('\nDelegacia com outliers inferiores')
    print(30*'=')
    if df_lesao_corp_outliers_inferiores.empty:
        print('Não há delegaicas com outliers inferiores')
    else:
        print(df_lesao_corp_outliers_inferiores.sort_values(
            by='lesao_corp_dolosa', ascending=True))

    # Imprime delegacias com outliers superiores
    print('\Delegacias com outliers superiores')
    print(30*'=')
    if df_lesao_corp_outliers_superiores.empty:
        print('Não há delegacias com outliers superiores')
    else:
        print(df_lesao_corp_outliers_superiores.sort_values(
            by='lesao_corp_dolosa', ascending=False))

except Exception as e:
    print(f'Erro ao salvar dados: {e}')
    exit()


#  MEDIDAS DE DISTRIBUICAO (ASSIMETRIA E CURTOSE)
try:
    print('\n\nDistribuição de lesões corporais dolosas')

    # Calcula assimetria e curtose
    assimetria = df_lesao_corp['lesao_corp_dolosa'].skew()
    curtose = df_lesao_corp['lesao_corp_dolosa'].kurtosis()

    print('\nMedidas de Distribuição...')
    print(30*'=')
    print(f'Assimetria: {assimetria:.3f}')
    print(f'Curtose: {curtose:.3f}')

except Exception as e:
    print(f'Erro ao obter medidas de distribuição: {e}')
    exit()


# MEDIDAS DE DISPERSÃO
# Desvio Padrão, Coeficiente Variação,
# Variância, Distância da Variância à Média
try:
    print('\n\nMedidas de Dispersão')

    variancia = np.var(array_lesoes_corp_dolosas)
    distancia_var_media = variancia / (media_lesoes_corp_dolosas ** 2)
    desvio_padrao = np.std(array_lesoes_corp_dolosas)
    coeficiente_variacao = desvio_padrao / media_lesoes_corp_dolosas

    # IMPRIME MEDIDAS DE DISPERSÃO
    print('\nMedidas de dispersão...')
    print(30*'=')
    print(f'Variância: {variancia:.3f}')
    print(f'Distância da variância para a média: {distancia_var_media:.3f}')
    print(f'Desvio padrão: {desvio_padrao:.3f}')
    print(f'Cóeficiente de variação: {coeficiente_variacao:.3f}')

except Exception as e:
    print(f'Erro ao obter medidas de dispersão: {e}')
    exit()


#  VERIFICAR CORRELAÇÃO (LESÕES DOLOSAS X CULPOSAS)
try:
    print('\n\nVerificar correlação entre lesões dolosas e culposas')

    # Calcula correlação entre as variáveis
    correlacao = np.corrcoef(
        df_lesao_corp['lesao_corp_dolosa'], df_lesao_corp['lesao_corp_culposa'])[0, 1]

    print('\nObtendo correlação...')
    print(30*'=')
    print(f'Correlação entre lesões dolosas e culposas: {correlacao:.3f}')

except Exception as e:
    print(f'Erro ao obter correlação: {e}')
    exit()


# VISUALIZAÇÃO DOS DADOS
try:
    print('\n\nVISUALIZAÇÃO DOS DADOS')
    print(30*'=')
    print('Obtendo visualização dos dados...\n')

    # Matplotlib
    plt.subplots(2, 2, figsize=(18, 10))
    plt.suptitle('Análise Lesão Corporal Dolosa e Lesão Corporal Culposa')

    # Posição 1: Scatter plot - Correlação entre lesões dolosas e culposas
    plt.subplot(2, 2, 1)
    plt.scatter(df_lesao_corp['lesao_corp_dolosa'],
                df_lesao_corp['lesao_corp_culposa'], c='red')
    plt.title('Lesão Corporal Dolosa e Culposa')

    # Posição 2: Histograma - Lesões dolosas
    plt.subplot(2, 2, 2)
    plt.hist(array_lesoes_corp_dolosas, bins=100, edgecolor='blue')
    plt.title('Histograma Lesão Corporal Dolosa')

    # Posição 3: Barras - Outliers superiores ou 10 DPs
    plt.subplot(2, 2, 3)

    if df_lesao_corp_outliers_superiores.empty:
        top10_cisp = df_lesao_corp.sort_values(
            by='lesao_corp_dolosa', ascending=False).head(10)

        # Criação do gráfico de Barras Horizontal
        plt.barh(top10_cisp['cisp'].astype(str),
                 top10_cisp['lesao_corp_dolosa'], color='red')

        # Adicionando rótulos com o valor de lesão_corp_dolosa
        for i, v in enumerate(top10_cisp['lesao_corp_dolosa']):
            plt.text(v + 10, i, f'{v}', color='black',
                     va='center')  # Mostra apenas o valor

        plt.title('Top 10 - Maiores Registros (Delegacia)')

    else:
        df_lesao_corp_outliers_superiores_ordenados = df_lesao_corp_outliers_superiores.sort_values(
            by='lesao_corp_dolosa', ascending=True)

        # Criação do gráfico de barras horizontal
        plt.barh(df_lesao_corp_outliers_superiores_ordenados['cisp'].astype(str),
                 df_lesao_corp_outliers_superiores_ordenados['lesao_corp_dolosa'],
                 color='red')

        # Adicionando rótulos com o valor de lesão_corp_dolosa
        for i, v in enumerate(df_lesao_corp_outliers_superiores_ordenados['lesao_corp_dolosa']):
            plt.text(v + 10, i, f'{v}', color='black', va='center')

        plt.title('Delegacias com Outiliers Superiores')

    # Ajustar layout para não sobrepor
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Posição 4: Medidas descritivas
    plt.subplot(2, 2, 4)

    # IMPRESSÃO DOS RESULTADOS
    plt.text(0.02, 0.9, f'Média: {media_lesoes_corp_dolosas:.3f}', fontsize=12)
    plt.text(0.02, 0.8, f'Mediana: {mediana_lesoes_corp_dolosas}', fontsize=12)
    plt.text(0.02, 0.7, f'Distância (Média e Mediana): {distancia:.3f}', fontsize=12)
    plt.text(0.02, 0.6, f'Menor registro de lessões dolosas: {minimo}', fontsize=12)
    plt.text(0.02, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
    plt.text(0.02, 0.4, f'Q1 - 25% das Delegacias registraram menos que: {q1}', fontsize=12)
    plt.text(0.02, 0.3, f'Q3 - 75% das Delegacias registrarão menos que: {q3}', fontsize=12)
    plt.text(0.02, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
    plt.text(0.02, 0.1, f'Maior Registro de lessões dolosas: {maximo}', fontsize=12)
    plt.text(0.7, 0.9, f'Amplitude Total: {amplitude_interquartilica}', fontsize=12)
    plt.text(0.7, 0.8, f'Correlação: {correlacao:.3f}', fontsize=12)
    plt.text(0.7, 0.7, f'Assimetria: {assimetria:.3f}', fontsize=12)
    plt.text(0.7, 0.6, f'Curtose: {curtose:.3f}', fontsize=12)
    plt.text(0.7, 0.5, f'Variância: {variancia:.3f}', fontsize=12)
    plt.text(0.7, 0.4, f'Distância var x média: {distancia_var_media:.3f}', fontsize=12)
    plt.text(0.7, 0.3, f'Desvio padrão: {desvio_padrao:.3f}', fontsize=12)
    plt.text(0.7, 0.2, f'Coef. variação: {coeficiente_variacao}', fontsize=12)

    # Título
    plt.title('Análise Descritiva')

    # Desativar os eixos
    plt.axis('off')

    # Ajustar espaçamento no lauyout
    plt.tight_layout(rect=[0, 0.01, 1, 0.95])

    # Exibir painel gráfico
    plt.show()

except Exception as e:
    print(f'Erro ao obter medidas de dispersão: {e}')
    exit()


# PRINT DOS QUESTIONAMENTOS
print(60*'=')
print('QUAL MÉDIA É CONFIÁVEL?')
print(60*'=')
print(f'Com correlação calculada em {correlacao:.3f}, indica que existe uma\n'
      f'forte correlação entre as lesões, o que significa que, em geral, \n'
      f'quando o número de lesões corporais dolosas aumenta, o número de \n'
      f'lesões corporais culposas também tende a aumentar\n')

print(f'Há uma grande variabilidade nos dados, tornando a média menos \n'
      f'representativa. Neste caso, a mediana {mediana_lesoes_corp_dolosas} \n'
      f'é mais adequada, pois é menos sencível aos outliers. Como a \n'
      f'assimetria dos dados está em {assimetria:.3f}, acredito que a mediana, \n'
      f'seja mais confiável')
print(60*'-', '\n')

print(60*'=')
print('A PARTIR DE QUAL QTD AS MENORES OCORRÊNCIAS?')
print(60*'=')
print(f'As DPs com Menores Registros de Ocorrências estão abaixo do primeiro \n'
      f'quartil, no valor de {q1}\n')

print(f'O terceiro quatil foi calculado em {q3}. Isso quer dizer, que 75% das \n'
      f'DPs registraram menos de {q3} ocorrências')
print(60*'-', '\n')

print(60*'=')
print('A PARTIR DE QUAL QTD AS MAIORES OCORRÊNCIAS?')
print(60*'=')
print(f'As DPs com Maiores Registros de Ocorrências estão acima do \n'
      f'do limite superior calculado em {limite_superior} ')
print(60*'-')
