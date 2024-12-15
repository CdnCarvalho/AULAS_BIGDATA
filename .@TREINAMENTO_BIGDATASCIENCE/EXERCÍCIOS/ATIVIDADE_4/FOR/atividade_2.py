# 05 - PREVISÃO DO TEMPO
# Este programa verifica a previsão do tempo para os próximos 5 dias e informa se deve aproveitar ou não.

# Lista com as previsões para os próximos 5 dias
previsoes = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]  

# Percorre cada previsão
for previsao in previsoes:  
    if previsao == "Ensolarado":  # Verifica se a previsão é ensolarada
        print("Aproveite e passeie!")  # Mensagem para dia ensolarado
    else:  # Para previsões diferentes de ensolarado
        print("Não esqueça o guarda-chuva!")  # Mensagem para dias não ensolarados



# 06 - CÁLCULO DE MÉDIA E RESULTADO FINAL
# Este programa calcula a média das notas de um aluno e informa se foi aprovado, está em recuperação ou reprovado.

# Inicializa a soma das notas
soma_das_notas = 0  

# Loop para solicitar 4 notas
for i in range(4):  
    nota = float(input(f"Digite a nota {i + 1}: "))  # Solicita a nota ao usuário
    soma_das_notas += nota  # Adiciona a nota à soma total

# Calcula a média
media = soma_das_notas / 4  

# Verifica a situação do aluno com base na média
if media >= 7.0:  # Aprovado
    print("Aprovado!")  
elif media >= 5.0:  # Em recuperação
    print("Em recuperação!")  
else:  # Reprovado
    print("Reprovado!")  
