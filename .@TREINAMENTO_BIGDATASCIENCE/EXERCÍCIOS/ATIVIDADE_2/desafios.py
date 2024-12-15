# ATIVIDADE AVALIATIVA

# MÉDIA PARA APROVAÇÃO
# Este programa calcula a média de 4 notas e determina a situação do aluno.

# Solicita as 4 notas do aluno
nota1 = float(input("Digite a primeira nota: "))  
nota2 = float(input("Digite a segunda nota: "))  
nota3 = float(input("Digite a terceira nota: "))  
nota4 = float(input("Digite a quarta nota: "))  

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4  

# Verifica a situação do aluno com base na média
if media > 7:  
    print("Aprovado")  # Se a média for maior que 7, exibe "Aprovado"
elif media >= 5:  
    print("Recuperação")  # Se a média estiver entre 5 e 7, exibe "Recuperação"
else:
    print("Reprovado")  # Se a média for menor que 5, exibe "Reprovado"




# AUMENTO DE SALÁRIO
# Este programa calcula o aumento de salário com base no cargo do funcionário.

# Solicita o cargo do funcionário
cargo = input("Digite o cargo do funcionário: ").strip().lower()  # Converte a entrada para minúsculas e remove espaços

# Solicita o salário atual do funcionário
salario_atual = float(input("Digite o salário atual: "))  

# Determina o percentual de aumento com base no cargo
if cargo == "serviços gerais":  
    percentual_aumento = 0.50  # Aumento de 50%
elif cargo == "vigia":  
    percentual_aumento = 0.30  # Aumento de 30%
elif cargo == "recepcionista":  
    percentual_aumento = 0.25  # Aumento de 25%
elif cargo == "vendedor":  
    percentual_aumento = 0.15  # Aumento de 15%
else:
    percentual_aumento = 0  # Caso o cargo não esteja listado, não há aumento

# Calcula o novo salário
novo_salario = salario_atual * (1 + percentual_aumento)  

# Exibe o novo salário
print(f"O novo salário é: R$ {novo_salario:.2f}")  # Mostra o novo salário formatado com 2 casas decimais




# EXERCÍCIO 04: ORDENANDO NÚMEROS
# Este programa recebe 3 números inteiros e os exibe em ordem crescente.

# Recebe os 3 números inteiros
numero1 = int(input("Digite o primeiro número: "))  
numero2 = int(input("Digite o segundo número: "))  
numero3 = int(input("Digite o terceiro número: "))  

# Cria uma lista com os números e ordena
numeros = [numero1, numero2, numero3]  # Coloca os números em uma lista
numeros.sort()  # Ordena a lista em ordem crescente

# Exibe os números ordenados
print("Números em ordem crescente:", numeros)  # Mostra os números já ordenados




# VERIFICAÇÃO DE GÊNERO
# Este programa verifica o gênero com base na letra digitada.

# Solicita que o usuário digite uma letra
genero = input("Digite F para feminino ou M para masculino: ").upper()  # Recebe a entrada do usuário e transforma em maiúscula

# Verifica a letra digitada e exibe a mensagem correspondente
if genero == "F":  
    print("Feminino")  # Se a entrada for "F", exibe "Feminino"
elif genero == "M":  
    print("Masculino")  # Se a entrada for "M", exibe "Masculino"
else:
    print("Outros")  # Para qualquer outra letra, exibe "Outros"




# DESAFIO 02: JOGO DA ADIVINHAÇÃO
# Este programa faz o computador escolher um número e pede para o usuário adivinhar.

import random  # Importa a biblioteca random para gerar números aleatórios

# O computador "pensa" em um número entre 0 e 10
numero_secreto = random.randint(0, 10)  # Gera um número aleatório entre 0 e 10

# Solicita que o usuário tente adivinhar o número
palpite = int(input("Tente adivinhar o número entre 0 e 10: "))  

# Verifica se o palpite está correto
if palpite == numero_secreto:  
    print("Você venceu!")  # Se o palpite for igual ao número secreto, o usuário venceu
else:
    print("Você perdeu! O número era:", numero_secreto)  # Se não, informa o número secreto
