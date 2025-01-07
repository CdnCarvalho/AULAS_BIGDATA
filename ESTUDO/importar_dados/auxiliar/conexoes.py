import os
import pandas as pd
import polars as pl
import mysql.connector as mysql
from dotenv import load_dotenv
# - mysql.connector: Biblioteca para conexão com o mysql
# - pip install mysql.connector
# - Também podemos conectar usando o SQLAlchemy, usando o pymysql


# - POLARS > http://pola.rs
# - Polars é uma biblioteca de manipulação de dados projetada para lidar com
#   grandes volumes de dados de forma eficiente.
# - Utiliza multithreading paralelismo no processamento, maximizando o uso da
# - CPU e seus núcleos, resultando em maior desempenho p/ operações intensivas.
# - A biblioteca gerencia internamente a pseudo-distribuição dos dados,
#   otimizando o fluxo de processamento.
# - Os dados são armazenados em DataFrames Polars, uma estrutura altamente
#   otimizada para manipulações rápidas e eficientes.
# - Além disso, Polars se destaca por sua interface intuitiva e suporte
#   a análises avançadas, ideal para trabalhar com Big Data.
# - pip install polars

# - PANDAS > https://pandas.pydata.org/
# - Pandas é outra biblioteca amplamente utilizada para análise e
#   manipulação de dados.
# - É ideal para dados de tamanho pequeno a médio, sendo amplamente usada
#   em projetos de Data Science, Machine Learning e análises exploratórias.
# - Com Pandas, os dados são manipulados em estruturas chamadas Series
#   (dados unidimensionais) e DataFrames (dados bidimensionais).
# - Embora menos eficiente em volumes massivos de dados, Pandas é extremamente
#   flexível e amplamente suportada pela comunidade.
# - pip install pandas


'''Funções Personalizadas para Obter Dados'''

# - A função abaixo é utilizada p/ obter dados utilizando Polars.
# - Utilizamos a palavra reservada "def" para criar uma função em Python.
# - Esta função suporta arquivos Excel e CSV, dependendo do tipo especificado
def obter_dados_pl(endereco_arquivo, nome_arquivo, tipo_arquivo, separador):
    # Verifica o tipo do arquivo p/ escolher o método apropriado do Polars.
    try:
        endereco_nome_arquivo = f'{endereco_arquivo}{nome_arquivo}'
        # Carrega dados de um arquivo Excel
        if tipo_arquivo == 'excel':
            df = pl.read_excel(endereco_nome_arquivo)
        # Carrega dados de um arquivo CSV com um separador especificado
        elif tipo_arquivo == 'csv':
            df = pl.read_csv(
                endereco_nome_arquivo,
                separator=separador,
                encoding='utf8-lossy'  # Especifica a codificação do arquivo
            )
        else:
            # Caso o tipo de arquivo não seja suportado, exibe uma mensagem de
            # erro e não retorna nada
            print('Tipo de arquivo não suportado!')
            return None

        # - Retorna o DataFrame carregado
        return df
    except ImportError as e:
        # Captura e exibe erros de importação ou de leitura de arquivos
        print("Erro ao obter dados - função obter_dados: ", e)
        return None


# - A função abaixo obtem dados utilizando PANDAS
# - Assim como a função anterior, esta função suporta arquivos Excel e CSV.
def obter_dados_pd(endereco_arquivo, nome_arquivo, tipo_arquivo, separador):
    # - Verifica o tipo do arquivo para escolher o método apropriado do Pandas.
    try:
        endereco_nome_arquivo = f'{endereco_arquivo}{nome_arquivo}'
        # - Verifica se é um arquivo Excel
        if tipo_arquivo == 'excel':
            df = pd.read_excel(endereco_nome_arquivo)
        # - Verifica se é um um arquivo CSV
        elif tipo_arquivo == 'csv':
            # - Carrega dados de um arquivo CSV com separador especificado
            df = pd.read_csv(
                endereco_nome_arquivo,
                sep=separador,
                encoding='iso-8859-1'
            )
        else:
            # Caso o tipo de arquivo não seja suportado, exibe uma msg de erro
            print('Tipo de arquivo não suportado!')
            return None
        
        # Retorna o DataFrame carregado
        return df
    except ImportError as e:
        # Captura e exibe erros de importação ou de leitura de arquivos
        print("Erro ao obter dados - função obter_dados: ", e)
        return None


# - Esta função conecta aos dados em um banco de dados MySQL
# - Esta função: Conecta, Executa a consulta e retorna os dados.
def obter_dados_mysql(query):
    try:
        # - Carrerga as variáveis do arquivo .env p/ serem pegas pelo Python
        load_dotenv()

        # - Pegando as variáveis de ambiente
        hostname = os.getenv('HOSTNAME')
        usuario = os.getenv('USER')
        senha = os.getenv('PASSWORD')
        banco = os.getenv('DATABASE')

        # - Conectando no MySQL
        # - Variável de conexão são conhecidas como instância
        #   de banco de dados
        conexao = mysql.connect(
            host=hostname,  # Endereço do servidor do banco de dados
            user=usuario,  # Usuário do banco de dados
            password=senha,  # Senha do banco de dados
            database=banco  # Nome do banco de dados
        )

        # Executa a consulta SQL, usando a query passada pelo usuário.
        # Retorna os resultados em DataFrame do Pandas
        df = pd.read_sql(query, conexao)
        return df
    
    except ImportError as e:
        # Captura e exibe erros relacionados à conexão ou execução da consulta
        print("Erro ao obter dados do MySQL: ", e)
        return None