import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 35, 29],  # Quantitativa
    'Gênero': ['F', 'M', 'F'],  # Qualitativa
    'Altura': [1.70, 1.80, 1.65]  # Quantitativa
}

df = pd.DataFrame(data)


print(f'\n {df}') # printando o dataframe

# PRINTANDO VARIÁVEIS QUANTITATIVAS

# IDADE
print('\nVARIÁVEIS QUANTITATIVAS')
print(30*'=')

print('Idade: ')
s_idade = pd.Series(df['Idade'])
print(s_idade.values)
# print(df['Idade'].values)

# ALTURA
print('\nAltura: ')
s_aultura = pd.Series(df['Altura'])  # quantitativa (ALTURA)
print(s_aultura.values)


# PRINTANDO VARIÁVEIS QUALITATIVAS

# GÊNERO
print('\n VARIÁVEIS QUALITATIVAS')
print(30*'=')
print('Gênero: ')
s_genero = pd.Series(df['Gênero'])
print(s_genero.values)