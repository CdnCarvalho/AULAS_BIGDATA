import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Demilitando somente as variáveis munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    # Somando roubo_veiculo por município
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

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
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # filtrar o dataframe df_roubo_veiculo para os municípios 
    # com outliers superiores (valores discrepantes)
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]

    # Printando municípios com outliers Inferiores
    print('\nMunicípios com outliers inferiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True))

    print('\nMunicípios com outliers superiores: ')
    print(30*'-')
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))

except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()


# Medidas de distribuição
try:
    print('Calculando medidas de distribuição...')

    # Assimentria. Skewness
    # É uma medida que descreverá o quanto uma distribuição é simétrica ou assimétrica
    # Quanto mais próximo de 0 (-0.5 a 0.5), mais simétrica é a distribuição e
    # os dados estão distribuídos de forma homogênea     # ao redor da média.
    # Acima de 0.5, a assimetria é positiva, os dados estão mais concentrados na parte menor da distribuição.
    # Os dados maiores estão puxando a média para cima. A Média tende a ser maior que a mediana.
    # 0.5 a 1.0 é uma assimetria moderada.
    # Assimetria acima 1.0 é uma assimetria alta
    # Abaixo de -0.5, a assimetria é negativa, os dados estão mais concentrados na parte maior da distribuição.
    # Os dados menores estão puxando a média para baixo. A média tende a ser menor que a mediana.
    # -0.5 a -1.0 é uma assimetria moderada.
    # Assimetria abaixo -1.0 é uma assimetria alta
    assimetria = df_roubo_veiculo['roubo_veiculo'].skew()

    # Curtose. Kurtosis
    curtose = df_roubo_veiculo['roubo_veiculo'].kurtosis()

    print('\nMedidas de distribuição: ')
    print(30*'-')
    print(f'Assimetria: {assimetria}')
    print(f'Curtose: {curtose}')

except Exception as e:
    print(f'Erro ao calcular as medidas de distribuição: {e}')
    exit()

# Medidas de dispersão
try:
    print('Calculando medidas de dispersão...')

    # É uma medida para obsersar a dispersão dos dados.
    # Observa-se em relação a média.
    # É a média dos quadrados das diferenças entre cada valor e a média.
    # O resultado da variância está elevado ao quadrado
    variancia = np.var(array_roubo_veiculo)

    # Distância da variância para a média
    distancia_var_media = variancia / (media_roubo_veiculo ** 2)

    # Devio padrão é a raiz quadrada da variância
    # Apresenta o quanto os dados estão afastados da média (para mais ou para menos).
    # Valor absoluto
    desvio_padrao = np.std(array_roubo_veiculo)

    # Coeficiente de variação
    # É a magnitude do desvio padrão em realção a média.
    # Escala percentual para dar esta magnitude.
    coef_variacao = desvio_padrao / media_roubo_veiculo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print(f'Variância: {variancia}')
    print(f'Dist. var x média: {distancia_var_media}')
    print(f'Desvio padrão: {desvio_padrao}')
    print(f'Coef. variação: {coef_variacao}')

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')
    exit()

# Visualizando dados
try: 
    # Criar uma figura com 1 linha e 2 colunas para visualização lado a lado
    plt.subplots(1, 2, figsize=(16, 7))  # Tamanho da figura definido em 16x7 polegadas
    # Título principal do gráfico
    plt.suptitle('Análise de roubo de veículos no RJ') 

    # Primeira subplot: Boxplot
    plt.subplot(1, 2, 1)  # Configurar o primeiro gráfico no lado esquerdo
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)  # Criar um boxplot horizontal, exibindo a média
    # Título específico para o boxplot
    plt.title('Boxplot dos Dados')

    # Segunda subplot: Exibição de informações estatísticas
    plt.subplot(1, 2, 2)  # Configurar o segundo gráfico no lado direito
    plt.text(0.1, 0.9, f'Média: {media_roubo_veiculo}', fontsize=12)
    plt.text(0.1, 0.8, f'Mediana: {mediana_roubo_veiculo}', fontsize=12)
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
    
    # Título específico para esta exibição de texto
    plt.title('Medidas Observadas') 

    # Desativar os eixos para o gráfico de texto
    plt.axis('off')  # Remove as linhas e marcas de eixo para focar somente nos textos

    # Ajustar o layout para evitar sobreposição entre elementos gráficos
    plt.tight_layout()  # Ajusta os subplots para usar o espaço disponível de forma eficiente

    # Exibir os gráficos criados
    plt.show()

except ImportError as e:
    print(f'Erro ao visualizar dados: {e}')
    exit()
