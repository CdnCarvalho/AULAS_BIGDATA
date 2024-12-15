import polars as pl

# Caminho do arquivo
ENDERECO_DADOS = r'./dados/'

# LazyFrame para carregar os dados
df_dados = pl.read_csv(ENDERECO_DADOS + 'dados_teste.csv')

df_dados_lazy = df_dados.lazy()
# Consulta lazy
df_dados_resultado = (
    df_dados_lazy
    .filter(pl.col("regiao") == "SP")  # Filtrar vendas da região SP
    .group_by(["forma_pagamento"])       # Agrupar por forma de pagamento
    .agg((pl.col("quantidade") * pl.col("preco")).sum().alias("total_vendas"))  # Calcular total de vendas
)


# Mostrar o plano de execução
print("Plano de Execução:")
print(df_dados_resultado.explain())


# Executar e exibir o resultado
df_resultado = df_dados_resultado.collect()
print(df_resultado)