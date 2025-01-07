# configurações / pesquisar interactive / 
# Jupyter Interactive Window Text Edition Execute Selection

# importar pandas
import pandas as pd


# Obtendo os dados do ISP
try:
    # Endereço dos dados do isp
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Ler os dados
    df_isp = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # Ver as primeiras linhas
    print(df_isp.head())
except ImportError as e:
    print('Erro ao ler os dados:', e)
