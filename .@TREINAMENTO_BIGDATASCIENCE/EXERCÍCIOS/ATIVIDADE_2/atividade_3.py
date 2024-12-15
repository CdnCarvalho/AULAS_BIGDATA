# ATIVIDADE 1

# OPERADORES RELACIONAIS VERIFICANDO INTERVALOS 

# Verificação de número fora do intervalo (Usando not)
# Este programa recebe um número e verifica se ele não está no intervalo de 10 a 50.
numero = float(input("Digite um número: "))  # Solicita que o usuário digite um número

# Verifica se o número está fora do intervalo usando a negação (not)
if not (10 <= numero <= 50):  
    print("Fora do intervalo")  # Exibe mensagem se o número estiver fora do intervalo
else:
    print("Dentro do intervalo")  # Exibe mensagem se o número estiver dentro do intervalo



# ATIVIDADE 2

# Turno do Dia
# Este programa solicita ao usuário que digite a hora atual e determina se é manhã ou tarde/noite.
hora = int(input("Digite a hora atual (formato 24h): "))  # Recebe a hora em formato 24h

# Verifica se a hora está entre 6 e 12 (manhã)
if 6 <= hora < 12:  
    print("Manhã")  # Se a hora estiver entre 6 e 12, exibe "Manhã"
else:
    print("Tarde/Noite")  # Caso contrário, exibe "Tarde/Noite"



# ATIVIDADE 3

# OPERADORES LÓGICOS 

# Verificação de ano bissexto (Usando and e or)
# Este programa verifica se um ano é bissexto.
ano = int(input("Digite um ano: "))  # Solicita que o usuário digite um ano

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  
    print("Ano bissexto")  # Exibe se o ano é bissexto
else:
    print("Ano não bissexto")  # Exibe se o ano não é bissexto



# ATIVIDADE 4

# Verificação Masculino e Feminino
# Este programa solicita ao usuário que informe seu gênero e valida a entrada.

# Recebe a entrada do usuário e a transforma em maiúscula, pegando apenas o
# primeiro caracter para facilitar a comparação. "Isso ainda dar problema, se
# o usuário não digitar nada."
genero = input("Digite F para feminino ou M para masculino: ")[0].upper()  

# Valida, se a letra digitada é um dos valores esperados, M ou F, se não for, entra no Else.
if genero == "F" or genero == "M":  
    # Se a entrada for "F", exibe "Feminino"; se for "M", exibe "Masculino"
    if genero == "F":  
        print("Feminino")  
    else:  
        print("Masculino")  
else:
    # Exibe mensagem de erro se a entrada não for reconhecida
    print("Entrada inválida") 



# ATIVIDADE 5

# Verificação de senha e usuário (Usando and)
# Este programa solicita um nome de usuário e uma senha e verifica se estão corretos.
usuario = input("Digite o nome de usuário: ")  # Recebe o nome de usuário
senha = input("Digite a senha: ")  # Recebe a senha

# Verifica se o nome de usuário e a senha estão corretos
if usuario == "aline" and senha == "12345":  
    print("Acesso concedido")  # Exibe acesso concedido se ambos estão corretos
else:
    print("Acesso negado")  # Exibe acesso negado se algum dos dados estiver incorreto



# ATIVIDADE 6

# Verificação de múltiplos critérios para descontos (Usando or)
# Este programa verifica se a pessoa tem direito a um desconto em uma compra.
estudante = input("Você é estudante? (s/n): ").lower()  # Recebe a resposta se é estudante
professor = input("Você é professor? (s/n): ").lower()  # Recebe a resposta se é professor
valor_compra = float(input("Digite o valor da compra: "))  # Solicita o valor da compra

# Verifica se a pessoa tem direito a um desconto
if estudante == "s" or professor == "s" or valor_compra > 300:  
    print("Desconto aplicado")  # Exibe se o desconto é aplicado
else:
    print("Sem desconto")  # Exibe que não há desconto aplicado




# ATIVIDADE 7

# VERIFICAR SE UM NÚMERO ESTÁ ENTRE DOIS VALORES (USANDO AND)
# Este programa verifica se um número está entre 10 e 20 (inclusive).

# Solicita ao usuário que digite um número e 
# converte a entrada para um valor decimal

numero = float(input("Digite um número: "))

# Verifica se o número está dentro do intervalo de 10 a 20
# usando operadores lógicos
if numero >= 10 and numero <= 20:  
    # A condição verifica se o número é maior ou igual a 10 E menor ou igual a 20
    print("Número dentro do intervalo")  # Exibe mensagem se o número está no intervalo
else:
    # Se a condição anterior não for atendida, o número está fora do intervalo
    print("Número fora do intervalo")  # Exibe mensagem se o número está fora do intervalo




# ATIVIDADE 8

# Verificar se o voto é obrigatório ou facultativo (Usando or)
# Este programa verifica se o voto é obrigatório ou facultativo com base na idade.
idade = int(input("Digite sua idade: "))  # Solicita a idade do usuário

# Verifica se o voto é obrigatório ou facultativo
if 18 <= idade <= 70:  
    print("Voto Obrigatório")  # Exibe se o voto é obrigatório
elif 16 <= idade < 18 or idade > 70:  
    print("Voto Facultativo")  # Exibe se o voto é facultativo
else:
    print("Idade inválida")  # Exibe mensagem para idades que não se encaixam nas opções



# ATIVIDADE 9

# Verificar se uma pessoa pode se aposentar (Usando and e or)
# Este programa verifica se uma pessoa pode se aposentar com base na idade 
# e no tempo de contribuição.
idade = int(input("Digite sua idade: "))  # Solicita a idade do usuário
tempo_contribuicao = int(input("Digite seu tempo de contribuição em anos: "))  # Solicita o tempo de contribuição

# Verifica se a pessoa pode se aposentar
if idade >= 65 or tempo_contribuicao >= 30:  
    print("Pode se aposentar")  # Exibe se a pessoa pode se aposentar
else:
    print("Ainda não pode se aposentar")  # Exibe se a pessoa ainda não pode se aposentar
