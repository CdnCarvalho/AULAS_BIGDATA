# 1. Reajuste de Salário
# Este programa recebe o salário, código do funcionário e cargo, e calcula o novo salário com base no percentual de aumento.

# Solicita informações do funcionário
codigo = int(input("Digite o código do funcionário: "))  # Código do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))  # Salário do funcionário

# Inicializa as variáveis de cargo e novo salário
cargo = ""
novo_salario = 0.0

# Verifica o código do funcionário e calcula o novo salário
match codigo:
    case 1:  # Serviços Gerais
        cargo = "Serviços Gerais"
        novo_salario = salario * 1.5  # Aumento de 50%
    case 2:  # Vigia
        cargo = "Vigia"
        novo_salario = salario * 1.3  # Aumento de 30%
    case 3:  # Recepcionista
        cargo = "Recepcionista"
        novo_salario = salario * 1.25  # Aumento de 25%
    case 4:  # Vendedor
        cargo = "Vendedor"
        novo_salario = salario * 1.15  # Aumento de 15%
    case _:  # Código inválido
        print("Código de funcionário inválido!")
        exit()  # Encerra o programa se o código for inválido

# Exibe o cargo e o novo salário
print(f"Cargo: {cargo}")
print(f"Novo salário: R$ {novo_salario:.2f}")




# 2. CONSUMO DE COMBUSTÍVEL
# Este programa calcula o consumo estimado de combustível para diferentes tipos de moto.

# Solicita o percurso e tipo de moto
percurso = float(input("Digite o percurso em quilômetros: "))  # Percurso em km
tipo_moto = input("Digite o tipo de moto (A, B ou C): ").upper()  # Tipo da moto

# Calcula o consumo estimado de combustível
match tipo_moto:
    case "A":  # Tipo A
        consumo = percurso / 26  # Consumo em litros
    case "B":  # Tipo B
        consumo = percurso / 20  # Consumo em litros
    case "C":  # Tipo C
        consumo = percurso / 7  # Consumo em litros
    case _:  # Tipo inválido
        print("Tipo de moto inválido!")
        exit()  # Encerra o programa se o tipo de moto for inválido

# Exibe o consumo estimado
print(f"Consumo estimado: {consumo:.2f} litros")




# 3. CÁLCULO DE IMPOSTO DE RENDA
# Este programa calcula o imposto de renda com base na faixa salarial.

# Solicita o salário do usuário
salario = float(input("Digite o salário: R$ "))  # Salário do usuário

# Calcula o imposto de renda
if salario <= 2000:
    imposto = 0  # Isento
elif salario <= 5000:
    imposto = salario * 0.10  # 10%
else:
    imposto = salario * 0.20  # 20%

# Exibe o imposto de renda a ser pago
print(f"Imposto de renda: R$ {imposto:.2f}")
