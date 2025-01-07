import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # - Selecionando Variáveis
    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa','lesao_corp_morte']]

    # Totalizando as lesões
    df_total_lesoes = df_lesoes.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_morte']).reset_index()

    print(df_total_lesoes.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# Calculando a correlação
try:
    print('Calculando a correlação...')

    correlacao = np.corrcoef(df_total_lesoes['lesao_corp_dolosa'], df_total_lesoes['lesao_corp_morte'])[0, 1]

    print(f'Correlação: {correlacao}')

    # - Plotar gráfico
    plt.scatter(df_total_lesoes['lesao_corp_dolosa'], df_total_lesoes['lesao_corp_morte'])
    plt.title(f'Correlação: {correlacao}')
    plt.xlabel('Lesão corporal dolosa')
    plt.ylabel('Lesão corporal seguida de morte')

    plt.show()

except ImportError as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()