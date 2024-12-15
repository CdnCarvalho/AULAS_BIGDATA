import pandas as pd

# Lendo um arquivo Excel com o método read_excel (deve apontar para o arquivo real)
df = pd.read_excel('vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas da planilha Excel:")
print(df.head())

# Valor máximo de faturamento total
print("\nMaior valor de faturamento total:")
print(df['Faturamento Total (R$)'].max())

# Valor menor de faturamento
print("\nMenor valor de faturamento:")
print(df['Faturamento Total (R$)'].min())

# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(df['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df['Preço por Unidade (R$)'].mean())