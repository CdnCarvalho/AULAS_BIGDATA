import pandas as pd

# Criando um dicionário com os dados. As chaves representam os nomes das colunas e os valores são listas com os dados.
data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.65]
}

# Criando um DataFrame a partir do dicionário 'data'. 
# O DataFrame organiza os dados em uma tabela.
df = pd.DataFrame(data)

# Exibindo o DataFrame completo com todas as colunas: Nome, Idade, Gênero e Altura
print(f'\n {df}')

# PRINTANDO VARIÁVEIS QUANTITATIVAS
print('\nVARIÁVEIS QUANTITATIVAS') 
print(30*'=')

# Exibindo a coluna 'Idade', que contém dados numéricos, uma variável quantitativa
print('Exibindo Idade: ')
print(df['Idade'])

# Exibindo a coluna 'Altura', outra variável quantitativa, também com dados numéricos
print('\nExibindo Altura: ')
print(df['Altura'])

# PRINTANDO VARIÁVEIS QUALITATIVAS
print('\nVARIÁVEIS QUALITATIVAS')
print(30*'=')  

# Exibindo a coluna 'Gênero', que contém valores categóricos, uma variável qualitativa
print('Exibindo Gênero: ')
print(df['Gênero'])
