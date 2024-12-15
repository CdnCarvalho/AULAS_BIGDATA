# 1) Programa para ler 5 números e calcular dobro, triplo e quádruplo 
# (usando while e loop infinito)

# 01 - CÁLCULO DE NÚMEROS
# Este programa lê 5 números e calcula seu dobro, triplo e quádruplo.

cont = 0  # Contador de números lidos
while cont < 5:  # Limita a 5 iterações
    numero = float(input("Digite um número: "))  # Lê um número
    print(f"Dobro: {numero * 2}, Triplo: {numero * 3}, Quádruplo: {numero * 4}")  # Exibe os resultados
    cont += 1  # Incrementa o contador

# Loop infinito (com controle)
cont = 0
while True:
    if cont >= 5:  # Verifica se 5 números foram lidos
        break  # Sai do loop
    numero = float(input("Digite um número: "))  # Lê um número
    print(f"Dobro: {numero * 2}, Triplo: {numero * 3}, Quádruplo: {numero * 4}")  # Exibe os resultados
    cont += 1  # Incrementa o contador



# 2) Programa com menu para realizar operações com dois valores
# 02 - MENU DE OPERAÇÕES
# Este programa lê dois valores e apresenta um menu de operações.

while True:
    # Lê os dois valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    # Menu de opções
    print("\nEscolha uma opção:")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print(f"Soma: {valor1 + valor2}")
    elif opcao == 2:
        print(f"Multiplicação: {valor1 * valor2}")
    elif opcao == 3:
        maior = valor1 if valor1 > valor2 else valor2
        print(f"Maior: {maior}")
    elif opcao == 4:
        continue  # Volta ao início do loop para novos números
    elif opcao == 5:
        print("Saindo do programa...")
        break  # Sai do loop
    else:
        print("Opção inválida! Tente novamente.")



# 3) Programa para ler produtos e calcular total, produtos acima de R$1000 e o mais barato
# 03 - CONTROLE DE PRODUTOS
# Este programa lê produtos e calcula total gasto, produtos acima de R$1000 e o mais barato.

total_gasto = 0.0
cont_produtos_acima_1000 = 0
nome_produto_mais_baro = ""
preco_produto_mais_barato = float('inf')  # Inicializa como infinito

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))

    # Atualiza o total gasto
    total_gasto += preco

    # Verifica se o produto custa mais de R$1000
    if preco > 1000:
        cont_produtos_acima_1000 += 1

    # Verifica se é o produto mais barato
    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco
        nome_produto_mais_baro = nome

    continuar = input("Deseja continuar? (sim/não): ").strip().lower()
    if continuar != "sim":
        break  # Sai do loop

# Exibe os resultados
print(f"\nTotal gasto: R$ {total_gasto:.2f}")
print(f"Produtos acima de R$1000: {cont_produtos_acima_1000}")
print(f"Produto mais barato: {nome_produto_mais_baro} (R$ {preco_produto_mais_barato:.2f})")



# 4) Programa para cadastrar pessoas e calcular informações
# 04 - CADASTRO DE PESSOAS
# Este programa lê a idade e sexo de várias pessoas e calcula informações.

cont_pessoas_maior_18 = 0
cont_homens = 0
cont_mulheres_menor_20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    # Verifica as condições para contagem
    if idade > 18:
        cont_pessoas_maior_18 += 1
    if sexo == "M":
        cont_homens += 1
    if sexo == "F" and idade < 20:
        cont_mulheres_menor_20 += 1

    continuar = input("Deseja continuar? (sim/não): ").strip().lower()
    if continuar != "sim":
        break  # Sai do loop

# Exibe os resultados
print(f"\nPessoas com mais de 18 anos: {cont_pessoas_maior_18}")
print(f"Homens cadastrados: {cont_homens}")
print(f"Mulheres com menos de 20 anos: {cont_mulheres_menor_20}")
