import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obter dados
try:
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Ler o arquivo CSV
    df_ocorrencias = pd.read_csv(
        ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Filtrar apenas as variáveis de delegacia e recuperações de veículos
    df_recup_veiculo = df_ocorrencias[['cisp', 'recuperacao_veiculos']]

    # Agrupar por delegacia e somar os valores de recuperações
    df_recup_veiculo = df_recup_veiculo.groupby(['cisp']).sum().reset_index()

    print(df_recup_veiculo.head())
    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Distribuição dos dados
try:
    print('Descrevendo a distribuição dos dados...')
    array_recup_veiculo = np.array(df_recup_veiculo['recuperacao_veiculos'])

    # Medidas de Tendência Central
    media = np.mean(array_recup_veiculo)
    mediana = np.median(array_recup_veiculo)
    distancia_media_mediana = (media - mediana) / mediana

    # Medidas de Posição e Dispersão
    q1 = np.quantile(array_recup_veiculo, 0.25, method='weibull')
    q3 = np.quantile(array_recup_veiculo, 0.75, method='weibull')
    iqr = q3 - q1
    minimo = np.min(array_recup_veiculo)
    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)
    maximo = np.max(array_recup_veiculo)
    amplitute_total = maximo - minimo

    # Identificar outliers superiores e inferiores
    df_recup_veiculo_outliers_sup = df_recup_veiculo[
        df_recup_veiculo['recuperacao_veiculos'] > limite_superior]

    df_recup_veiculo_outliers_inf = df_recup_veiculo[
        df_recup_veiculo['recuperacao_veiculos'] < limite_inferior]

    # Selecionar as 10 delegacias com valores abaixo de Q1
    df_recup_veiculo_baixo_q1 = df_recup_veiculo[
        df_recup_veiculo['recuperacao_veiculos'] < q1]
    df_recup_veiculo_baixo_q1 = df_recup_veiculo_baixo_q1.sort_values(
        # Ordena e pega as 10 menores
        by='recuperacao_veiculos', ascending=True).head(10)

    # Exibir os gráficos para os outliers
    # Define a área do gráfico com 1 linha e 2 colunas
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico de outliers inferiores (ou as 10 delegacias abaixo de Q1, se não houver outliers)
    if not df_recup_veiculo_outliers_inf.empty:
        # Se há outliers inferiores, exibe-os
        axes[0].bar(df_recup_veiculo_outliers_inf['cisp'],
                    df_recup_veiculo_outliers_inf['recuperacao_veiculos'], color='blue')
    else:
        # Caso não haja outliers, exibe as 10 delegacias com valores abaixo de Q1
        axes[0].bar(df_recup_veiculo_baixo_q1['cisp'],
                    df_recup_veiculo_baixo_q1['recuperacao_veiculos'], color='blue')
    axes[0].set_title(f'Delegacias abaixo {q1} ou Outliers Inferiores')
    # Remove textos e marcas dos eixos
    axes[0].tick_params(left=False, bottom=False,
                        labelleft=False, labelbottom=False)

    # Gráfico de outliers superiores
    axes[1].bar(df_recup_veiculo_outliers_sup['cisp'],
                df_recup_veiculo_outliers_sup['recuperacao_veiculos'], color='red')
    axes[1].set_title('Outliers Superiores')
    # Remove textos e marcas dos eixos
    axes[1].tick_params(left=False, bottom=False,
                        labelleft=False, labelbottom=False)
    # Ajuste para evitar sobreposição dos gráficos
    plt.tight_layout()
    # Exibe o gráfico
    plt.show()

except ImportError as e:
    print(f'Erro ao descrever os dados: {e}')
    exit()
