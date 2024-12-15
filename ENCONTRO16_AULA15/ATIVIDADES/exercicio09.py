import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from auxiliar.conexoes import obter_dados_pd

# Constante do Endereço dos dados
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter dados
# comma separeted values (CSV), em português é valores separados por vírgulas
# mas, que nem sempre são vírgulas. É preciso verificar
try:
    print('Obtendo dados de ocorrências...')

    # parâmentros: endereco_arquivo, nome_arquivo, tipo_arquivo, separador
    df_ocorrencias = obter_dados_pd(ENDERECO_DADOS,'','csv',';')
    
    #print(df_ocorrencias.head()) #head sem valor, trará as 5 primeiras linhas

    print('Dados obtidos com sucesso!')
except ImportError as e:
    print('Erro ao obter dados: ', e)
    exit()

# delimitar somente as variáveis solicitadas e totalizar
try:
    print("inciando a delimitação das variáveis e a totalização...")
    # cidade e roubo de veículos
    #print(df_ocorrencias.columns) # exibir o nome de todas as colunas
    df_veiculos = df_ocorrencias[['cisp','roubo_veiculo','recuperacao_veiculos']]

    # totalizar o dataframe
    df_total_veiculos = df_veiculos.groupby('cisp')\
                            .sum(['roubo_veiculo','recuperacao_veiculos']).reset_index()
    
    print(df_total_veiculos)

    print('Delimitação e totalização concluídas!')
except ImportError as e:
    print("Erro ao delimitar o dataframe: ", e)
    exit()

# correlação dos dados
try:
    print('Analisando dados...')

    array_roubo_veiculo = np.array(df_total_veiculos['roubo_veiculo'])
    array_recuperacao_veiculos = np.array(df_total_veiculos['recuperacao_veiculos'])

    correlacao = np.corrcoef(array_roubo_veiculo,array_recuperacao_veiculos)[0,1]

    print('Correlação: ', correlacao)

except Exception as e:
    print("Erro ao analisar dados: ", e)
    exit()