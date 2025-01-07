import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# - Obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # - Encoding - utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # - Delimitando somente as variáveis
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # Totalizar por CISP
    df_total_veiculos = df_veiculos.groupby(['cisp']).sum(['roubo_veiculo', 'recuperacao_veiculos']).reset_index()

    print(df_total_veiculos.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()


# - Correlação
try:
    print('Calculando a correlação...')

    # - Correlação de pearson
    array_roubo_veiculo = np.array(df_total_veiculos['roubo_veiculo'])
    array_recuperacao_veiculos = np.array(df_total_veiculos['recuperacao_veiculos'])
    
    correlacao = np.corrcoef(array_roubo_veiculo, array_recuperacao_veiculos)[0, 1]

    print(f'Correlação: {correlacao}')

    # - Plotar gráfico
    plt.scatter(df_total_veiculos['roubo_veiculo'], df_total_veiculos['recuperacao_veiculos'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Roubo de Veículos')
    plt.ylabel('Recuperação de Veículos')

    plt.show()

except ImportError as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()