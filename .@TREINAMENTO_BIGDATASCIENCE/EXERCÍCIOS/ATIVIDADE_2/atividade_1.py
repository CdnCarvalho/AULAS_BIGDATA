# ATIVIDADE 1

# 1) Maioridade:
# Programa que recebe a idade de uma pessoa e verifica se é maior de idade (18 anos ou mais).
# Exibe uma mensagem informando se é maior de idade ou menor de idade.

idade = int(input("Digite sua idade: "))  # Solicita a idade do usuário

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade.")  # Mensagem para maior de idade
else:
    print("Você é menor de idade.")  # Mensagem para menor de idade


#


# 2) Verificação qual é o maior:
# Programa que lê dois números inteiros e verifica qual é o maior.
# Mostra os dois números na saída, informando qual é o maior.

# Solicita o primeiro número
numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))  # Solicita o segundo número

# Verifica qual número é maior
if numero1 > numero2:
    print(f"O maior número é {numero1}.")  # Mensagem com o maior número
else:
    print(f"O maior número é {numero2}.")  # Mensagem com o maior número


#


# 3) Verificação de número par ou ímpar:
# Programa que lê um número inteiro e verifica se ele é par ou ímpar.
# Exibe uma mensagem indicando o resultado.

# Solicita um número inteiro
numero = int(input("\nDigite um número inteiro: "))

# Verifica se o número é par, aplicando o resto da divisão por 2,
# se o resto for 0, é par, caso ano contrário é ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # Mensagem se o número é par
else:
    print(f"O número {numero} é ímpar.")  # Mensagem se o número é ímpar


#


# 4) Desconto em uma compra:
# Programa que pergunta o valor de uma compra.
# Se o valor for maior que 250 reais, aplica um desconto de 16% e exibe o valor final.
# Caso contrário, exibe o valor original sem desconto.

# Solicita o valor da compra
valor_compra = float(input("\nDigite o valor da compra: R$ "))

# Verifica se o valor da compra é maior que 250
if valor_compra > 250:
    desconto = valor_compra * 0.16  # Calcula o desconto de 16%
    valor_final = valor_compra - desconto  # Calcula o valor final após o desconto
    # Exibe o valor final com desconto
    print(f"Valor com desconto: R$ {valor_final:.2f}")
else:
    # Exibe o valor original
    print(f"Valor sem desconto: R$ {valor_compra:.2f}")


#


# 5) Verificação de idade para habilitação:
# Programa que pede a idade do usuário e informa se ele pode ou não
# se inscrever em uma autoescola.

# Solicita a idade para habilitação
idade_autoescola = int(input("\nDigite sua idade para habilitação: "))

# Verifica se a idade é suficiente para habilitação
if idade_autoescola >= 18:
    # Mensagem para quem pode se inscrever
    print("Você pode se inscrever na autoescola.")
else:
    # Mensagem para quem não pode se inscrever
    print("Você não pode se inscrever na autoescola.")


#


# 6) Cálculo da área de uma figura geométrica:
# Programa que pergunta se o usuário deseja calcular a área de um quadrado ou triângulo.
# Solicita os valores necessários e calcula a área.
# O método strip() é usado para remover espaços em branco no início e no final da string.
opcao = input("\nDeseja calcular a área de um quadrado ou triângulo? ").strip(
).lower()  # Solicita a figura

if opcao == "quadrado":  # Verifica se a escolha é quadrado
    # Solicita o valor do lado
    lado = float(input("Digite o valor do lado do quadrado: "))
    area_quadrado = lado ** 2  # Calcula a área do quadrado
    # Exibe a área do quadrado
    print(f"A área do quadrado é: {area_quadrado:.2f}")

elif opcao == "triângulo":  # Verifica se a escolha é triângulo
    # Solicita a base do triângulo
    base = float(input("Digite a base do triângulo: "))
    # Solicita a altura do triângulo
    altura = float(input("Digite a altura do triângulo: "))
    area_triangulo = (base * altura) / 2  # Calcula a área do triângulo
    # Exibe a área do triângulo
    print(f"A área do triângulo é: {area_triangulo:.2f}")
else:
    print("Opção inválida.")  # Mensagem para opção inválida


#


# 7) Verifica número Positivo e Negativo (Parte 1)
# Programa que pede um valor e mostra na tela se o valor é positivo ou negativo.

valor = float(input("\nDigite um valor: "))  # Solicita um valor ao usuário

# Verifica se o valor é maior que 0
if valor > 0:
    print(f"O valor {valor} é positivo.")  # Mensagem se o valor é positivo
elif valor < 0:
    print(f"O valor {valor} é negativo.")  # Mensagem se o valor é negativo
else:
    print("O valor é zero.")  # Mensagem se o valor é zero


#


# 8) Verifica número Positivo e Negativo (Parte 2)
# Implementa a funcionalidade de não aceitar o número 0.

# Solicita um valor ao usuário
valor = float(input("\nDigite um valor (não pode ser 0): "))

# Verifica se o valor é diferente de zero
if valor == 0:
    print("O valor 0 não é aceito.")  # Mensagem para valor zero
else:
    # Verifica se o valor é positivo ou negativo
    if valor > 0:
        print(f"O valor {valor} é positivo.")  # Mensagem se o valor é positivo
    else:
        print(f"O valor {valor} é negativo.")  # Mensagem se o valor é negativo
