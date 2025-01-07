# import pandas as pd
import polars as pl
from datetime import datetime
# pip install polars

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

