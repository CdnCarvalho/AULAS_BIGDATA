# DESAFIO: CLASSIFICAÇÃO DE PREVISÕES DO TEMPO
# Este programa classifica os dias da semana como ensolarados ou sem sol.

# Lista de dias da semana e suas previsões
dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
previsoes = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]

# Listas para armazenar os resultados
dias_ensolarados = []  
dias_sem_sol = []  

# Percorre as previsões e classifica os dias
for i in range(len(previsoes)):
    if previsoes[i] == "Ensolarado":  # Verifica se o dia é ensolarado
        dias_ensolarados.append(dias_da_semana[i])  # Adiciona o dia à lista de ensolarados
    else:  # Caso contrário, é um dia sem sol
        dias_sem_sol.append(dias_da_semana[i])  # Adiciona o dia à lista de sem sol

# Exibe os resultados
print("Dias Ensolarados:")
for dia in dias_ensolarados:
    print(dia)  # Mostra os dias ensolarados

print("\nDias Sem Sol:")
for dia in dias_sem_sol:
    print(dia)  # Mostra os dias sem sol
