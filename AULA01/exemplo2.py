import pandas as pd

# Criando uma lista de quantidades em estoque para diferentes produtos
produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera']
quantidade_estoque = [15, 30, 20, 10, 25]

# Criando uma série no Pandas
estoque = pd.Series(quantidade_estoque, index=produtos)

# Exibindo a série
print("Série Estoque de Produtos:")
print(estoque)

# Selecionando um valor específico pelo índice
print("\nQuantidade de notebooks em estoque:")
print(estoque['Notebook'])

# # Selecionando múltiplos valores
print("\nEstoque de Notebook e Câmera:")
print(estoque[['Notebook', 'Câmera']].values)

# Filtrando produtos com estoque abaixo de 20
print("\nProdutos com estoque abaixo de 20 unidades:")
print(estoque[estoque < 20])

# Operação aritmética: aumentar estoque em 5 unidades
print("\nAumentando o estoque em 5 unidades para todos os produtos:")
print(estoque + 5)

# Incluindo um valor nulo para simular a falta de dados
estoque.loc['Headphone'] = None
print("\nEstoque com um valor nulo (Headphone):")
print(estoque)

# Operações Aritméticas entre Séries
# Criando outra série com preços dos produtos
precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

# # Calculando o valor total do estoque (preço * quantidade)
print("\nValor total do estoque por produto (preço * quantidade):")
print(precos * estoque)
