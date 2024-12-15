# 01 - CONTAGEM REGRESSIVA PARA O ESTOURO DOS FOGOS
# Este programa exibe uma contagem regressiva de 10 a 0, com uma pausa de 1 segundo entre os números.


import time  # Importa o módulo time para utilizar a função sleep

for i in range(10, -1, -1):  # Contagem regressiva de 10 a 0
    print(i)  # Exibe o número atual
    time.sleep(1)  # Pausa de 1 segundo




# 02 - DIVISORES DE UM NÚMERO
# Este programa solicita um número ao usuário e exibe todos os seus divisores.

numero = int(input("Digite um número: "))  # Solicita um número inteiro ao usuário

print(f"Divisores de {numero}:")  # Exibe a mensagem inicial

for i in range(1, numero + 1):  # Percorre os números de 1 até o número fornecido
    if numero % i == 0:  # Verifica se o número é divisor
        print(i)  # Exibe o divisor




# 03 - CONTAGEM DE VOGAIS EM UMA FRASE
# Este programa conta quantas vezes as vogais a, e, i, o, u aparecem em uma frase fornecida pelo usuário.

frase = input("Digite uma frase: ")  # Solicita uma frase ao usuário
vogais = "aeiou"  # Define as vogais a serem contadas
contador_vogais = 0  # Inicializa o contador de vogais

# Percorre cada letra na frase
for letra in frase.lower():  # Converte a frase para minúsculas
    if letra in vogais:  # Verifica se a letra é uma vogal
        contador_vogais += 1  # Incrementa o contador

# Exibe o total de vogais encontradas
print(f"A quantidade de vogais na frase é: {contador_vogais}")




# 04 - REMOÇÃO DE VOGAIS DE UMA FRASE
# Este programa remove todas as vogais de uma frase digitada pelo usuário.

frase = input("Digite uma frase: ")  # Solicita uma frase ao usuário
vogais = "aeiouAEIOU"  # Define as vogais a serem removidas
frase_sem_vogais = ""  # Inicializa a nova frase sem vogais

# Percorre cada letra na frase
for letra in frase:  # Verifica cada letra da frase original
    if letra not in vogais:  # Se a letra não for uma vogal
        frase_sem_vogais += letra  # Adiciona a letra à nova frase

# Exibe a frase sem vogais
print("Frase sem vogais:", frase_sem_vogais)

