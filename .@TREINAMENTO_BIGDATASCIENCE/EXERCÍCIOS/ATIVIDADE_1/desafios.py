# DESAFIO 01
# 1 - Crie um programa que solicite um valor em real ao usuário
# e converta esse valor para as seguintes moedas:
# Dólar, Euro, Libra Esterlina, Dólar Canadense, Peso Argentino, Peso Chileno.

# Solicitando o valor em reais
valor_reais = float(input("Digite o valor em reais: R$ "))

# Cotações aproximadas (podem variar com o tempo, pesquisar valores atualizados)
cotacao_dolar = 4.90
cotacao_euro = 5.30
cotacao_libra = 6.20
cotacao_dolar_canadense = 3.80
cotacao_peso_argentino = 0.02
cotacao_peso_chileno = 0.006

# Realizando as conversões
valor_dolar = valor_reais / cotacao_dolar
valor_euro = valor_reais / cotacao_euro
valor_libra = valor_reais / cotacao_libra
valor_dolar_canadense = valor_reais / cotacao_dolar_canadense
valor_peso_argentino = valor_reais / cotacao_peso_argentino
valor_peso_chileno = valor_reais / cotacao_peso_chileno

# Exibindo os resultados formatados
print(f"\nO valor em Dólar: US$ {valor_dolar:.2f}")
print(f"O valor em Euro: € {valor_euro:.2f}")
print(f"O valor em Libra Esterlina: £ {valor_libra:.2f}")
print(f"O valor em Dólar Canadense: C$ {valor_dolar_canadense:.2f}")
print(f"O valor em Peso Argentino: $ {valor_peso_argentino:.2f}")
print(f"O valor em Peso Chileno: CLP$ {valor_peso_chileno:.2f}")




# DESAFIO 02
# 2 - Caixa eletrônico:
# O programa pergunta o valor do saque e informa quantas notas de cada valor serão fornecidas.
# As notas disponíveis são de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo é de 600 reais.

# Solicitando o valor do saque
valor_saque = int(input("\nDigite o valor do saque (entre 10 e 600 reais): "))

if 10 <= valor_saque <= 600:
    # Calculando a quantidade de notas (usando a divisao inteira. Exemplo: se o resultado
    # for decimal, o python ficará somente com o valor inteiro)
    notas_100 = valor_saque // 100
    valor_saque %= 100
    notas_50 = valor_saque // 50
    valor_saque %= 50
    notas_10 = valor_saque // 10
    valor_saque %= 10
    notas_5 = valor_saque // 5
    valor_saque %= 5
    notas_1 = valor_saque // 1

    # Exibindo o resultado
    print(f"\nNotas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 1: {notas_1}")
else:
    print("Valor inválido! O valor deve estar entre 10 e 600 reais.")
