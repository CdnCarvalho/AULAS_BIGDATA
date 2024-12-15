# ATIVIDADE 02
# ESTRUTURA DE DECISÃO ANINHADA
# OPERADORES RELACIONAIS 

# 1. Calculadora de Divisão:
# Escreva um algoritmo que leia dois números (dividendo e divisor) e informe se o resultado é positivo ou negativo. 
# Impossível dividir por 0.
dividendo = float(input("Digite o dividendo: "))  # Lê o dividendo como um número de ponto flutuante
divisor = float(input("Digite o divisor: "))  # Lê o divisor como um número de ponto flutuante

if divisor == 0:  # Verifica se o divisor é zero
    print("Impossível dividir por 0.")  # Mensagem de erro para divisão por zero
else:
    resultado = dividendo / divisor  # Realiza a divisão
    if resultado >= 0:  # Verifica se o resultado é positivo
        print(f"O resultado da divisão é {resultado}, que é positivo.")  # Mensagem para resultado positivo
    else:
        print(f"O resultado da divisão é {resultado}, que é negativo.")  # Mensagem para resultado negativo



# 2. Ataque do Personagem:
# Escreva um programa que receba uma string digitada pelo usuário;
# Caso a string seja "medieval", exiba no console "espada";
# Caso contrário, se a string for "futurista", exiba no console "sabre de luz";
# Caso contrário, exiba no console "Tente novamente".

# Lê a string do usuário e normaliza para minúsculas. O método strip() remove espaços em branco no início e no final da string.
tipo_arma = input("Digite o tipo de arma (medieval ou futurista): ").strip().lower()  

if tipo_arma == "medieval":  # Verifica se a string é "medieval"
    print("espada")  # Exibe mensagem para arma medieval
elif tipo_arma == "futurista":  # Se não for medieval, verifica se é "futurista"
    print("sabre de luz")  # Exibe mensagem para arma futurista
else:
    print("Tente novamente")  # Mensagem para entrada inválida




# 3. Verificação de idade para habilitação:
# Escreva um programa que peça a idade do usuário, pergunte se ele possui
# habilitação e com base nas duas respostas,
# informe se ele está apto ou não apto para dirigir.

idade_usuario = int(input("Digite sua idade: "))  # Lê a idade do usuário como um número inteiro
habilitacao = input("Você possui habilitação? (sim/não): ").strip().lower()  # Pergunta se possui habilitação

if idade_usuario >= 18 and habilitacao == "sim":  # Verifica se a idade é maior ou igual a 18 e se possui habilitação
    print("Você está apto para dirigir.")  # Mensagem para apto a dirigir
else:
    print("Você não está apto para dirigir.")  # Mensagem para não apto a dirigir


# 4. Classificação de temperatura:
# Escreva um programa que receba a temperatura em graus Celsius e classifique-a da seguinte forma:
# Abaixo de 10°C: "Frio"
# Entre 10°C e 30°C: "Agradável"
# Acima de 30°C: "Quente"
temperatura = float(input("Digite a temperatura em graus Celsius: "))  # Lê a temperatura como um número de ponto flutuante

if temperatura < 10:  # Verifica se a temperatura é menor que 10
    print("Frio")  # Mensagem para temperatura fria
elif 10 <= temperatura <= 30:  # Verifica se a temperatura está entre 10 e 30
    print("Agradável")  # Mensagem para temperatura agradável
else:  # Se não for nem fria nem agradável, é quente
    print("Quente")  # Mensagem para temperatura quente


# 5. Notas e conceitos:
# Faça um programa que leia a nota de um aluno e atribua um conceito de acordo com a seguinte regra:
# Nota maior ou igual a 7: "Aprovado"
# Nota entre 5 e 6.9: "Recuperação"
# Nota menor que 5: "Reprovado"
nota = float(input("Digite a nota do aluno: "))  # Lê a nota do aluno como um número de ponto flutuante

if nota >= 7:  # Verifica se a nota é maior ou igual a 7
    print("Aprovado")  # Mensagem para aprovado
elif 5 <= nota < 7:  # Verifica se a nota está entre 5 e 6.9
    print("Recuperação")  # Mensagem para recuperação
else:  # Se não for aprovado nem em recuperação, é reprovado
    print("Reprovado")  # Mensagem para reprovado


# 6. Classificação de IMC (Índice de Massa Corporal):
# Escreva um programa que calcule o IMC de uma pessoa (IMC = peso / altura²) e classifique o resultado em uma das categorias:
# O programa deve solicitar ao usuário o peso (em kg) e a altura (em metros), calcular o IMC e exibir a categoria correspondente conforme os valores acima.
peso = float(input("Digite o peso em kg: "))  # Lê o peso como um número de ponto flutuante
altura = float(input("Digite a altura em metros: "))  # Lê a altura como um número de ponto flutuante
imc = peso / (altura ** 2)  # Calcula o IMC

if imc < 18.5:  # Verifica se o IMC é menor que 18.5
    print("Abaixo do peso")  # Mensagem para abaixo do peso
elif 18.5 <= imc < 25:  # Verifica se o IMC está entre 18.5 e 24.9
    print("Peso normal")  # Mensagem para peso normal
elif 25 <= imc < 30:  # Verifica se o IMC está entre 25.0 e 29.9
    print("Sobrepeso")  # Mensagem para sobrepeso
else:  # Se for maior ou igual a 30
    print("Obesidade")  # Mensagem para obesidade


# 7. Classificação de idade para eventos esportivos:
# Crie um programa que receba a idade de uma pessoa e classifique-a em uma das
# categorias esportivas:
# O programa deve solicitar a idade da pessoa e exibir a categoria adequada.
# Caso a idade não se encaixe nas faixas etárias específicas, exiba uma
# mensagem padrão como "Idade fora da faixa etária permitida".

idade_evento = int(input("Digite sua idade: "))  # Lê a idade como um número inteiro

if idade_evento <= 12:  # Verifica se a idade é até 12 anos
    print("Infantil")  # Mensagem para infantil
elif 13 <= idade_evento <= 17:  # Verifica se a idade está entre 13 e 17 anos
    print("Juvenil")  # Mensagem para juvenil
elif 18 <= idade_evento <= 29:  # Verifica se a idade está entre 18 e 29 anos
    print("Adulto")  # Mensagem para adulto
elif idade_evento > 29:  # Verifica se a idade é acima de 29 anos
    print("Veterano")  # Mensagem para veterano
else:
    print("Idade fora da faixa etária permitida")  # Mensagem para idade fora da faixa
