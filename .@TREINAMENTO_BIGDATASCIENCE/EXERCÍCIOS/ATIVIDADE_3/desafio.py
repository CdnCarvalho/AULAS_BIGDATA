# 1. CONVERSÃO DE TEMPERATURA
# Este programa converte uma temperatura fornecida em Celsius para Fahrenheit ou Kelvin.

# Apresenta o menu de opções
print("Menu de Conversão de Temperatura:")
print("1. Converter de Celsius para Fahrenheit")
print("2. Converter de Celsius para Kelvin")

# Solicita a escolha do usuário
opcao = input("Escolha uma opção (1 ou 2): ")

# Solicita a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Realiza a conversão de acordo com a escolha do usuário
match opcao:
    case "1":  # Celsius para Fahrenheit
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f} °F")
    case "2":  # Celsius para Kelvin
        temperatura_kelvin = temperatura_celsius + 273.15
        print(f"A temperatura em Kelvin é: {temperatura_kelvin:.2f} K")
    case _:  # Opção inválida
        print("Opção inválida! Escolha 1 ou 2.")




# 2. CÁLCULO DE MÉDIA ESCOLAR
# Este programa calcula a média das notas e verifica a situação do estudante.

# Solicita as notas das duas avaliações normais
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

# Verifica se a nota optativa foi informada
if nota_optativa != -1:
    # Substitui a menor nota pela nota optativa
    menor_nota = min(nota1, nota2)
    media = (nota1 + nota2 + nota_optativa - menor_nota) / 2
else:
    # Se não fez a optativa, calcula a média simples
    media = (nota1 + nota2) / 2

# Exibe a média e a situação do estudante
print(f"Média: {media:.2f}")

if media >= 6.0:
    print("Aprovado")
elif media < 3.0:
    print("Reprovado")
else:
    print("Em exame")




# 3. CÁLCULO DO RENDIMENTO DO TÁXI
# Este programa calcula o rendimento do carro de um motorista de táxi.

# Define o preço do combustível
preco_combustivel = 4.87

# Solicita as informações do motorista
odometro_inicial = float(input("Digite a marcação do odômetro no início do dia (km): "))
odometro_final = float(input("Digite a marcação do odômetro no final do dia (km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total (R$) recebido dos passageiros: "))

# Calcula a média de consumo em km/L e o lucro líquido
distancia_percorrida = odometro_final - odometro_inicial
media_consumo = distancia_percorrida / litros_gastos
lucro_liquido = valor_recebido - (litros_gastos * preco_combustivel)

# Exibe os resultados
print(f"Média do consumo: {media_consumo:.2f} km/L")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")
