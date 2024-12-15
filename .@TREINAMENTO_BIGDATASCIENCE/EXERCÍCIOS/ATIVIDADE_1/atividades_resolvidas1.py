# ATIVIDADE 01
# Desenvolva um algoritmo que faça perguntas ao usuário sobre seu nome e data de nascimento.
# Após coletar as informações, o programa deve exibir a mensagem: 
# "Olá fulano! Você nasceu no dia 'X' do mês 'Y' do ano 'Z'. A sua idade é ..."

# Perguntando o nome do usuário
nome = input("Digite seu nome: ")

# Perguntando o ano de nascimento
ano_nascimento = input("Digite o ano de nascimento (ex: 1990): ")

# Perguntando o mês de nascimento
mes_nascimento = input("Digite o mês de nascimento (ex: 07 para julho): ")

# Perguntando o dia de nascimento
dia_nascimento = input("Digite o dia de nascimento (ex: 15): ")

# Imprimindo a mensagem com os dados coletados
print(f"\nOlá {nome}!")
print(f"Você nasceu no dia {dia_nascimento} do mês {mes_nascimento} do ano {ano_nascimento}.")

# Perguntando o ano atual ao usuário
ano_atual = input("Digite o ano atual: ")

# Calculando a idade do usuário de forma simples, sem uso de datas
idade = int(ano_atual) - int(ano_nascimento)

# Exibindo a idade calculada
print(f"A sua idade é {idade} anos.")





# ATIVIDADE 02

# 1 - Elabore um algoritmo que leia um número e escreva na tela,
# além do próprio número, mostre também o anterior e o sucessor.

# Lendo um número do usuário
numero = int(input("Digite um número: "))

# Exibindo o número, seu anterior e seu sucessor
print(f"Número: {numero}")
print(f"Anterior: {numero - 1}")
print(f"Sucessor: {numero + 1}")



# 2 - Crie um programa que leia um número e mostre o seu dobro, o triplo e o seu quadrado.

# Lendo um número do usuário
numero = int(input("\nDigite um número: "))

# Calculando e exibindo o dobro, o triplo e o quadrado do número
print(f"Dobro: {numero * 2}")
print(f"Triplo: {numero * 3}")
print(f"Quadrado: {numero ** 2}")



# 3 - Implemente um algoritmo que leia as notas de teste e da prova de um aluno,
# retire a média e mostre o resultado na tela.

# Lendo as notas de teste e prova do aluno
nota_teste = float(input("\nDigite a nota do teste: "))
nota_prova = float(input("Digite a nota da prova: "))

# Calculando a média das notas
media = (nota_teste + nota_prova) / 2

# Exibindo a média
print(f"Média: {media}")



# 4 - Faça um programa que leia um número em metros e converta-o para centímetros e milímetros.

# Lendo o valor em metros
metros = float(input("\nDigite o valor em metros: "))

# Convertendo metros para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Exibindo o valor convertido
print(f"Centímetros: {centimetros} cm")
print(f"Milímetros: {milimetros} mm")



# 5 - Crie um algoritmo que leia um número e imprima a sua tabuada (até 10) na tela.

# Lendo o número do usuário
numero = int(input("\nDigite um número para ver a tabuada: "))

# Exibindo a tabuada do número de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




# ATIVIDADE 03

# 1 - Menu - Elabore um programa que mostre o seguinte menu na tela:
# Cadastro de Clientes
# 0 - Fim
# 1 - Inclui
# 2 - Altera
# 3 - Exclui
# 4 - Consulta
# Digite uma opção:
# Ao digitar um valor para a opção, o programa exibe qual opção foi escolhida.

print("Cadastro de Clientes")
print("0 - Fim")
print("1 - Inclui")
print("2 - Altera")
print("3 - Exclui")
print("4 - Consulta")

opcao = input("Digite uma opção: ")

# Exibindo a opção escolhida
print(f"\nVocê escolheu a opção '{opcao}'.")



# 2 - E os 10% do garçom?
# Defina uma variável para o valor de uma refeição que custou R$ 42,54;
# Defina uma variável para o valor da taxa de serviço que é de 10%;
# Defina uma variável que calcula o valor total da conta e exiba-o no console com essa formatação: R$ XXXX.XX.

valor_refeicao = 42.54
taxa_servico = 0.10
valor_total = valor_refeicao + (valor_refeicao * taxa_servico)

# Exibindo o valor total da conta com formatação
print(f"\nValor total da conta: R$ {valor_total:.2f}")




# 3 - Qual o valor do troco?
# Defina uma variável para o valor de uma compra que custou R$100,98;
# Defina uma variável para o valor que o cliente pagou R$150,00;
# Defina uma variável que calcula o valor do troco e exiba-o no console com o valor final arredondado.

valor_compra = 100.98
valor_pago = 150.00
valor_troco = valor_pago - valor_compra

# Exibindo o valor do troco arredondado
print(f"\nValor do troco: R$ {round(valor_troco, 2)}")




# 4 - Você está na flor da idade?
# Defina uma variável para o valor do ano do nascimento;
# Defina uma variável para o valor do ano atual;
# Defina uma variável que calcula o valor final da idade da pessoa;
# Exiba uma mensagem final dizendo a idade da pessoa e a mensagem "Você está na flor da idade".

ano_nascimento = int(input("\nDigite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento

# Exibindo a idade e a mensagem final
print(f"\nVocê tem {idade} anos. Você está na flor da idade!")




# ATIVIDADE 04

# 1 - Pensando em um boletim escolar.
# Criar um algoritmo que associe duas notas de estudantes a duas variáveis criadas,
# calcule a média desse estudante e guarde em uma terceira variável. Mostre o Resultado.

# Lendo as duas notas do estudante
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calculando a média das notas
media = (nota1 + nota2) / 2

# Exibindo a média
print(f"Média do estudante: {media:.2f}")




# 2 - Construir um algoritmo no qual o usuário digitará 2 números
# e o programa exibirá o resultado das quatro operações básicas da matemática
# (soma, subtração, divisão, multiplicação) e módulo.

# Lendo dois números do usuário
numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando as operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
modulo = numero1 % numero2

# Exibindo os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Módulo: {modulo}")



# 3 - Calculadora de aumento de aluguel.
# Vamos construir um programa que irá calcular o aumento anual do seu aluguel
# baseado no IGPM de 31%. A calculadora deve apresentar o aluguel reajustado
# no formato R$ XXXX.XX.

# Lendo o valor do aluguel
valor_aluguel = float(input("\nDigite o valor do aluguel: "))

# Calculando o aumento de 31%
aumento = valor_aluguel * 0.31
valor_reajustado = valor_aluguel + aumento

# Exibindo o valor do aluguel reajustado
print(f"Valor do aluguel reajustado: R$ {valor_reajustado:.2f}")



# ATIVIDADE 05

# 1 - Desenvolver um programa que calcule quantas polegadas há em um cubo com 1 × 1 × 1 milhas.

# Sabemos que:
# 1 milha = 5280 pés
# 1 pé = 12 polegadas

# Calculando quantas polegadas há em um cubo de 1 × 1 × 1 milhas
milhas = 5280
pes = milhas * 12
polegadas = pes ** 3

# Exibindo o resultado em polegadas cúbicas
print(f"\nCubo de 1x1x1 milhas contém {polegadas} polegadas cúbicas.")



# 2 - Usa o teorema de Pitágoras para encontrar o comprimento da hipotenusa,
# dados os comprimentos dos dois lados opostos (A = 3 m, B = 4 m, H = ?).

# Definindo os valores dos catetos
cateto_a = 3
cateto_b = 4

# Calculando a hipotenusa
hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5

# Exibindo o valor da hipotenusa
print(f"Comprimento da hipotenusa: {hipotenusa} m")
