import pandas as pd

# Passo 1: Criando uma série com as quantidades em estoque para diferentes tipos de roupas
# Definindo os produtos e as quantidades em estoque
produtos = ['Camiseta', 'Calça', 'Jaqueta', 'Vestido', 'Boné']
quantidade_estoque = [50, 30, 15, 10, 25]

# Criando a série no Pandas
estoque_roupas = pd.Series(quantidade_estoque, index=produtos)

# Exibindo a série criada
print("Estoque inicial de roupas:")
print(estoque_roupas)

# Passo 2: Adicionando uma nova peça de roupa com valor None
# Simulando a inclusão de um produto sem valor de estoque definido
estoque_roupas['Saia'] = None

# Exibindo a série com o valor nulo
print("\nEstoque de roupas (incluindo Saia, sem estoque definido):")
print(estoque_roupas)

# Passo 3: Selecionando os produtos com mais de 20 unidades em estoque
# Realizando a filtragem de produtos com mais de 20 unidades
produtos_com_estoque_alto = estoque_roupas[estoque_roupas > 20]

# Exibindo os produtos com estoque alto
print("\nProdutos com mais de 20 unidades em estoque:")
print(produtos_com_estoque_alto)

# Passo 4: Criando outra série com os preços dos produtos
# Definindo os preços dos produtos
precos_roupas = pd.Series([30.00, 80.00, 150.00, 120.00, 25.00], index=produtos)

# Exibindo a série de preços
print("\nPreços das roupas:")
print(precos_roupas)

# Passo 5: Calculando o valor total do estoque (preço * quantidade)
# Multiplicando as duas séries (estoque * preço) para obter o valor total do estoque
valor_total_estoque = precos_roupas * estoque_roupas

# Exibindo o valor total do estoque por produto
print("\nValor total do estoque por produto:")
print(valor_total_estoque)
