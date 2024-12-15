import pandas as pd

# Definindo o dataset com variáveis relacionadas a vendas
data = {
    'Código do Produto': [1, 2, 3, 4, 5, 6],  # Códigos como números
    
    'Produto': ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera', 'Fone de Ouvido'],
    
    # Quantitativa Discreta (Unidades Vendidas)
    'Unidades Vendidas': [120, 340, 210, 150, 80, 175],
    
    # Qualitativa Nominal (Cor do Produto)
    'Cor': ['Preto', 'Prata', 'Azul', 'Preto', 'Branco', 'Vermelho'],
    
    # Qualitativa Nominal (Categoria do Produto)
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Acessórios', 'Eletrônicos', 'Acessórios'],
    
    # Quantitativa Contínua (Preço por Unidade em R$)
    'Preço por Unidade (R$)': [3500.00, 2500.00, 1200.50, 900.75, 1500.00, 200.50],
    
    # Quantitativa Contínua (Faturamento Total em R$)
    'Faturamento Total (R$)': [420000.00, 850000.00, 252105.00, 135112.50, 120000.00, 35187.50],
    
    # Qualitativa Ordinal (Nível de Satisfação dos Clientes)
    'Satisfação': ['Alto', 'Muito Alto', 'Médio', 'Alto', 'Médio', 'Médio']
}

# Criando o DataFrame
df = pd.DataFrame(data)

# QUALITATIVAS
# Imprimindo variáveis Qualitativas
print("Imprimindo as Variáveis Qualitativas\n")

# Variáveis Qualitativas Nominais
print("---- Variáveis Qualitativas Nominais ----")
print('Código do Produto:')
print(df['Código do Produto'])

print('\nProduto:')
print(df['Produto'])

print('\nCor:')
print(df['Cor'])

print('\nCategoria:')
print(df['Categoria'])

# Variáveis Qualitativas Ordinais
print("\n---- Variáveis Qualitativas Ordinais ----")
print('Satisfação:')
print(df['Satisfação'])

# QUANTITATIVAS
# Imprimindo variáveis Quantitativas
print("\nImprimindo as Variáveis Quantitativas\n")

# Subtítulo: Variáveis Quantitativas Discretas
print("---- Variáveis Quantitativas Discretas ----")
print('Unidades Vendidas:')
print(df['Unidades Vendidas'])

# Subtítulo: Variáveis Quantitativas Contínuas
print("\n---- Variáveis Quantitativas Contínuas ----")
print('Preço por Unidade (R$):')
print(df['Preço por Unidade (R$)'])

print('\nFaturamento Total (R$):')
print(df['Faturamento Total (R$)'])
