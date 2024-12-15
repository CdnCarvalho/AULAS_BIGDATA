# 01 - SISTEMA DE CADASTRO DE ALUNOS
# Este programa permite cadastrar alunos, inserir suas notas e calcular suas médias.

# Inicializa as listas para armazenar nomes e médias dos alunos
nomes = []
medias = []

# Pergunta ao usuário se deseja cadastrar um aluno
cadastro = input("Deseja cadastrar um aluno? (sim/não): ").strip().lower()

while cadastro == "sim":
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ")  

    # Solicita as quatro notas do aluno
    nota1 = float(input("Digite a primeira nota: "))  
    nota2 = float(input("Digite a segunda nota: "))  
    nota3 = float(input("Digite a terceira nota: "))  
    nota4 = float(input("Digite a quarta nota: "))  

    # Calcula a média
    media = (nota1 + nota2 + nota3 + nota4) / 4  

    # Adiciona o nome e a média às listas
    nomes.append(nome)  
    medias.append(media)  

    # Pergunta se deseja cadastrar outro aluno
    cadastro = input("Deseja cadastrar outro aluno? (sim/não): ").strip().lower()  

# Exibe as listas de alunos e suas médias
print("\nLista de Alunos e suas Médias:")
for i in range(len(nomes)):  
    print(f"Aluno: {nomes[i]}, Média: {medias[i]:.2f}")  
