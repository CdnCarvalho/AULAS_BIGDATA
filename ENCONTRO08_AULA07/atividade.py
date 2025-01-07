import pandas as pd
import numpy as np


# PRIMEIRO TRY: -- Obter dados
try:
    print('Obtendo dados...')

    # OBTENDO CSV: VENDAS 2017 MIRANDA
    df_dados_vendas = pd.read_csv('tb_Vendas2017_Miranda.csv', sep=';', encoding='iso-8859-1')

    # Delimitando as variáveis - dataframe Vendas:
    df_vendas = df_dados_vendas[['Numero da Venda', 'ID Produto', 'ID Cliente', 'Quantidade Vendida']]
    print(df_vendas.head())

    # OBTENDO CSV: CADSTRO DE PRODUTOS 2017 MIRANDA
    df_dados_produtos = pd.read_csv('tb_CadastroProdutos2017_Miranda.csv', sep=';', encoding='utf-8')
    print(df_dados_produtos.head())
    
    # Delimitando as variáveis - dataframe de Produtos:
    df_produtos = df_dados_produtos[['Nome da Marca', 'Categoria', 'Preco Unitario', 'ID Produto']]
    print(df_produtos.head())
    
    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# SEGUNDO TRY: -- Preparar os dataframes
try:
    print('Preparando os dataframes')

    # # Converter 'ID Produto' em ambos os DataFrames para string usando .loc
    # df_vendas.loc[:, 'ID Produto'] = df_vendas['ID Produto'].astype(str)
    # df_produtos.loc[:, 'ID Produto'] = df_produtos['ID Produto'].astype(str)

    # Convertendo a coluna 'Preco Unitario' p/ número - Usando o método ".LOC" para modificar diretamente a coluna
    # No CSV o preço está separado por vírgula, então é necessário substituir a vírgula por ponto
    # Os : indicam que todos os registros da varável "coluna" serão todos modificados.
    # Float no final converte o valor para número decimal, através do método "astype" "como tipo" em português
    df_produtos.loc[:, 'Preco Unitario'] = df_produtos['Preco Unitario'].str.replace(',', '.').astype(float)

    # Configurando o formato de exibição de números decimais p/ 2 casas decimais
    pd.options.display.float_format = '{:.2f}'.format

    # Aplicando o Merge nos dataframes df_vendas e df_produtos
    # Usando a coluna 'ID Produto' como o compo em comum nos dois dataframe
    # Método pd.merge()
    df_produtos_vendidos = pd.merge(df_vendas, df_produtos, on='ID Produto')

    # Criando a coluna 'Valor Total' 
    # Calculando o 'Valor Total' = Preco Unitario * Quantidade Vendida
    df_produtos_vendidos['Valor Total'] = (df_produtos_vendidos['Quantidade Vendida'] * df_produtos_vendidos['Preco Unitario'])

    # Agrupando por ID ou Categoria do Produto
    # No agrupamento, algumas (atributos ou variáveis) "ou seja, COLUNAS" de cada registro, podem desaparecer.
    # Isso é umm efeito colateral do agrupamento. Exemplo: Em um agrupamento por Categoria, o ID Produto pode desaparecer.
    # O método .gg() "agregação" é necessário para calcular a soma da 'Quantidade Vendida' e 'Valor Total' para cada categoria.
    # No caso do 'ID Produto', não faz sentido calcular a soma de cada ID. O ID é uma variável Qualitativa.
    # No entanto, poderia fazer sentido contarmos quantos IDs existem em cada categoria. 
    # Para isso, usariamos o método .count() em vez de .sum().
    # Neste caso obteríamos o número de produtos vendidos em cada categoria.
    df_produtos_vendidos = df_produtos_vendidos.groupby('Categoria').agg({
        'Quantidade Vendida': 'sum',
        'Valor Total': 'sum'
    }).reset_index()

    # Exibindo as primeiras linhas do DataFrame resultante
    print(df_produtos_vendidos.head(20).sort_values(by='Valor Total', ascending=False))

except ImportError as e:
    print(f'Erro ao formatar e juntar os dataframes: {e}')
    exit()


# TERCEIRO TRY: - Realizando a análise dos dados com Numpy
try:
    print('Processando... ...')

    # ARRAY NUMPY
    array_produtos_vendidos = np.array(df_produtos_vendidos['Valor Total'])

    # Calcula a média de roubo
    media_produtos_vendidos = np.mean(array_produtos_vendidos)
    # Calcula mediana de roubo
    mediana_produtos_vendidos = np.median(array_produtos_vendidos)
    # Distânicia
    distancia = abs(
        (media_produtos_vendidos - mediana_produtos_vendidos) /
        mediana_produtos_vendidos
    ) * 100

    print('\nMedidas de tendência central: ')
    print(30*'-')
    print(f'Média do Valor Total: {media_produtos_vendidos}')
    print(f'Mediana de Valor Total: {mediana_produtos_vendidos}')
    print(f'Distância (Média e Mediana): {distancia}')

    # Medidas de dispersão
    maximo = np.max(array_produtos_vendidos)
    minimo = np.min(array_produtos_vendidos)
    amplitude = maximo - minimo

    print('\nMedidas de dispersão: ')
    print(30*'-')
    print('Máximo: ', maximo)
    print('Mínimo: ', minimo)
    print('Amplitude total: ', amplitude)

    # Quartis - Uso método weibull
    q1 = np.quantile(
        array_produtos_vendidos, 0.25, method='weibull')  # 25%
    q2 = np.quantile(
        array_produtos_vendidos, 0.50, method='weibull')  # 50%
    q3 = np.quantile(
        array_produtos_vendidos, 0.75, method='weibull')  # 75%

    # IQR (Intervalo interquartil)
    # É a amplitude do intervalo dos 50% dos dados centrais
    # Ela ignora os valores extremos. Não sofre a interferência dos mesmos
    # Máximo e Mínimo estão fora do IQR
    # Quanto mais próximo de zero, mais homogêneo são os dados
    # Quanto mais próximo do q3, mais heterogêneo são os dados
    iqr = q3 - q1

    # Limite Superior - Identificar os outliers acima de Q3
    limite_superior = q3 + (1.5 * iqr)

    # limite inferior Identifica os outliers abaixo de Q1
    limite_inferior = q1 - (1.5 * iqr)

    # Medidas de Posição (ou de Dispersão)
    print('\nMedidas de posição: ')
    print(30*'-')
    print('Menor valor de venda: ', minimo)
    print(f'Limite inferior: {limite_inferior}')
    print(f'25% das vendas estão abaixo de : {q1}')
    print(f'50% das vendas estão abaixo ou acima de : {q2}')
    print(f'25% das vendas estão acima de: {q3}')
    print(f'Amplitude InterQuartil (IQR): {iqr}')
    print(f'Limite superior: {limite_superior}')
    print('Maior valor das Vendas: ', maximo)

    # Filtrar o dataframe df_produtos_vendidos p/ obter outliers inferiores
    df_produtos_vendidos_outliers_inferiores = df_produtos_vendidos[
        df_produtos_vendidos['Valor Total'] < limite_inferior]

    # Filtrar o dataframe df_produtos_vendidos p/ obter outliers superiores
    df_produtos_vendidos_outliers_superiores = df_produtos_vendidos[
        df_produtos_vendidos['Valor Total'] > limite_superior]

    # Printando Outliers Inferiores
    print('\nOutliers inferiores: ')
    print(30*'-')
    if len(df_produtos_vendidos_outliers_inferiores) == 0:
        print('Não existem outliers inferiores!')
    else:
        print(df_produtos_vendidos_outliers_inferiores.sort_values(
            by='Valor Total', ascending=True))

    # Printando Outliers Superiores
    print('\nOutliers superiores: ')
    print(30*'-')
    if len(df_produtos_vendidos_outliers_superiores) == 0:
        print('Não existe outliers superiores!')
    else:
        print(df_produtos_vendidos_outliers_superiores.sort_values(
            by='Valor Total', ascending=False))

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()
