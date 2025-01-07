# importar pandas
import pandas as pd

# import polars as pl
# import polars as pl
from datetime import datetime

# Constante com o caminho do arquivo
ENDERECO_DADOS = './dados/csv/bolsa_fam/'

inicio = datetime.now()

df_dados = pd.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
# df_dados = pl.read_csv(ENDERECO_DADOS + '202401_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

# print(df_dados.head())
print(df_dados.columns)

# # Ordena o DataFrame pelo CPF em ordem crescente
# df_ordenado = df_dados.sort_values(by='CPF FAVORECIDO', ascending=True)

# # Exibe os primeiros registros para verificar a ordenação
# print(df_ordenado.head())

# # Opcional: salva o DataFrame ordenado em um novo arquivo CSV
# df_ordenado.to_csv(ENDERECO_DADOS + 'ordenado_por_cpf.csv', sep=';', encoding='iso-8859-1', index=False)

# # Agrupa os dados por estado e soma o valor das parcelas, ordenando em ordem decrescente
df_dados_estados = df_dados.groupby(['UF']).sum(['VALOR PARCELA'])
print(df_dados_estados)

fim = datetime.now()

print(f"Tempo de execução: {fim - inicio}")
