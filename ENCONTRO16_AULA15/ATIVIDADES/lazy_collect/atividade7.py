import polars as pl

# Caminho do arquivo
ENDERECO_DADOS = r'./dados/'

# LazyFrame para carregar os dados
df_dados = pl.read_csv(ENDERECO_DADOS + 'dados1.csv')

df_dados_lazy = df_dados.lazy()
# Consulta lazy
df_dados_resultado = (
    df_dados_lazy
    .group_by("regiao")
    .agg(((pl.col("quantidade") * pl.col("preco")).mean()).alias("ticket_medio"))  # Calcular ticket médio
    .sort("ticket_medio", descending=True)  # Ordenar por ticket médio
)

# Mostrar o plano de execução
print("Plano de Execução:")
print(df_dados_resultado.explain())

# Executar e exibir o resultado
df_resultado = df_dados_resultado.collect()
print(df_resultado)