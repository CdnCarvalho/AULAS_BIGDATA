# ALGORITMO PARA MÊS CORRESPONDENTE
# Este programa retorna o mês correspondente ao número digitado pelo usuário.

# Solicita que o usuário digite um número entre 1 e 12
numero_mes = int(input("Digite um número de 1 a 12: "))

# Usa o match/case para identificar o mês correspondente
match numero_mes:
    case 1:
        print("Janeiro")  # 1 corresponde a Janeiro
    case 2:
        print("Fevereiro")  # 2 corresponde a Fevereiro
    case 3:
        print("Março")  # 3 corresponde a Março
    case 4:
        print("Abril")  # 4 corresponde a Abril
    case 5:
        print("Maio")  # 5 corresponde a Maio
    case 6:
        print("Junho")  # 6 corresponde a Junho
    case 7:
        print("Julho")  # 7 corresponde a Julho
    case 8:
        print("Agosto")  # 8 corresponde a Agosto
    case 9:
        print("Setembro")  # 9 corresponde a Setembro
    case 10:
        print("Outubro")  # 10 corresponde a Outubro
    case 11:
        print("Novembro")  # 11 corresponde a Novembro
    case 12:
        print("Dezembro")  # 12 corresponde a Dezembro
    case _:
        # Caso o número não esteja entre 1 e 12
        print("Número inválido! Digite um número entre 1 e 12.")


# PROGRAMA DE RECOMENDAÇÃO DE PRATO TÍPICO
# Este programa recomenda um prato típico com base no tipo de restaurante escolhido pelo usuário.

# Solicita que o usuário escolha um tipo de restaurante
tipo_restaurante = input("Escolha um tipo de restaurante (Chinês, Italiano, Mexicano, Vegetariano): ").strip(
).title()  # Normaliza a entrada

# Usa o match/case para recomendar um prato
match tipo_restaurante:
    case "Chinês":
        print("Recomendamos: Frango Xadrez.")  # Prato típico chinês
    case "Italiano":
        print("Recomendamos: Lasanha.")  # Prato típico italiano
    case "Mexicano":
        print("Recomendamos: Tacos.")  # Prato típico mexicano
    case "Vegetariano":
        print("Recomendamos: Salada Caesar.")  # Prato típico vegetariano
    case _:
        # Caso o tipo não esteja listado
        print("Tipo de restaurante inválido! Escolha entre Chinês, Italiano, Mexicano ou Vegetariano.")


# ALGORITMO DE MENU INTERATIVO
# I Parte
# Crie um algoritmo como um menu com várias opções.
# O usuário escolherá uma delas para executar instruções específicas
# com base na opção selecionada. As opções são:
# 1.	"Adicionar Item"
# 2.	"Remover Item"
# 3.	"Listar Itens"
# 4.	"Sair"

#  A sua missão será fazer com que na saída, seja impressa uma
#  string informando a opção escolhida.
# Modifique, para que o algoritmo peça um valor ao usuário.
# Quando o usuário escolher uma das opções do menu, uma ação relativa seja realizada.


# Solicita que o usuário escolha uma opção
opcao = input("Escolha uma opção (1-4): ")

# Usa o match/case para imprimir a opção escolhida
match opcao:
    case "1":
        print("Você escolheu Adicionar Item.")
    case "2":
        print("Você escolheu Remover Item.")
    case "3":
        print("Você escolheu Listar Itens.")
    case "4":
        print("Você escolheu Sair.")
    case _:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")



# II Parte
# CONTINUAÇÃO (SEGUNDA PARTE)
# Modifique, para que o algoritmo peça um valor ao usuário. Quando o usuário
# escolher uma das opções do menu, uma ação relativa seja realizada.
# Este programa apresenta um menu com várias opções e executa ações baseadas em um valor inicial.

# Solicita que o usuário digite um valor inicial
valor_base = int(input("Digite um valor inicial: "))  # Lê o valor base fornecido pelo usuário

# Solicita que o usuário escolha uma opção
opcao = input("Escolha uma opção (1-4): ")

# Usa o match/case para executar a ação correspondente
match opcao:
    case "1":
        valor_base += 1  # Adiciona 1 ao valor base
        print(f"Valor atualizado após adicionar item: {valor_base}")
    case "2":
        valor_base -= 1  # Subtrai 1 do valor base
        print(f"Valor atualizado após remover item: {valor_base}")
    case "3":
        print(f"Valor atual: {valor_base}")  # Mostra o valor atual
    case "4":
        print("Saindo do programa...")  # Mensagem de saída
    case _:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")

