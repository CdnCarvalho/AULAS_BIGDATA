import pandas as pd
import polars as pl
from datetime import datetime
# pip install polars

# Recomendo acessar o site oficial para instalação do polars. http://pola.rs
# É uma biblioteca de manipulação de dados em larga escala, muito mais rápida, que o pandas. Desenvolvida em Rust.
# Ela é mais rápida, pois o processamento de dados é feito em paralelo, o que é muito mais eficiente que o processamento sequencial do pandas.
# A polars tem um motor de execução Multithread, que permite a execução de operações em paralelo.

try:
    ENDERECO_DADOS = r'./dados/'

    # hora de iníncio
    hora_import = datetime.now()

    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head())

    # hora final
    hora_impressao = datetime.now()

    print(f"Tempo de execução: {hora_impressao - hora_import}")
    
except ImportError as e:
    print("Erro ao obter dados: ", e)

