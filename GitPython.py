#Algoritmo -> sequencia de passos para executar uma tarefa!

#3 estruturas possiveis no algoritmo

#1 - Estrutural (Sequencia de passos contínuos)
#2 - Condicional (DECISAO - Vou executar um script se acontecer X e outro se Y)
#3 - Repetição - permite executar varias vezes o mesmo codigo

#variaveis
#espaços de memória que pode armazenar dados para a execução de um processo!

#tipos de variaveis
#Int, Float, String e Boolean
#Int (1 (so um valor)): Armazena valores inteiros (10, 14, 999, 362...)
#Float (1.(ponto)11(valor quebrado)) : Numeros decimais (1.2, 1.7, 3.98.... valores quebrados)
#String("", ''): cadeia de caracteres: "Rua dos Bobos n 0" são valores literais, ou seja 
#Não vou fazer calculos. Ex, bruno, gustavo, Kelvin, kaio, Luis, Fernanda, Nico
#"Rua nome da rua, n0"
#Regras-> uma string deve estar entre "",'', "house's Fer"
#boolean (true ou false) : é o poligrafo ele aceita dois valores true (verdadeiro) e false(falso)
# O paython tem a tipagem dinamica, ou seja ele entende 
# apartir do valor o tipo da variavel


#VARIAVEIS
#curso = 15.74
#a variavel "curso" recebe o valor "Manufatura Digital"

#exibir -> Comando Print
#print("Olá eu sou seu .py")

# #para conversar com o usuário eu uso o input
# altura = float(input("Digite sua altura"))
# #a variavel altura recebe um valor quebrado de altura

# print("sua altura é ")
# #exibe para mim a "FORMATAÇÃO" do texto com o valor de uma variavel

# nome = input("Digite seu nome ")
# sobrenome = input("Digite seu sobrenome")
# print(nome + sobrenome)
#para juntar duas strings uso o termo CONCATENAR


# print("Cadastro de uma pessoa")
# nome = input("Digite seu nome ")
# #idade = input("Digite sua idade ")
# endereco = input("Digite um endereço ")
# cpf = input("Digite seu CPF ")
# distancia = input("Digite a distancia percorrida no dia")
# anoNascimento = int(input("Digite o ano do seu nascimento"))
# idade = 2024 - anoNascimento
# print(idade)

#estrutura de algoritmo CONDICIONAL
#Executo alguma instrução de acordo com os dados que tenho. Por exemplo, só posso me alistar no exercito 
#se for maior de idade
#Para usar o IF e Else, eu tenho que saber quais as opções que eu tenho!

# if(idade >= 18):
# #se a idade for maior ou igual a 18 ENTÃO exiba a mensagem 
#     print("Você já pode se alistar")
# else:
# #se a idade não for maior ou igual a 18 ENTÃO(:) exiba a mensagem
#     print("Você é menor de idade")

# nota = float(input("Informe a Nota 1"))

# if (nota > 5):
#     print("Você está aprovado")
# elif(nota == 5):
#     print("Chama os pais, pq vc está no conselho")
# else:
#     print("Você está reprovado")


#se o salario for maior do que 1500 adicione 500
#se o salario for maior do que 2000 some 400
#se o salario for maior do que 3000 some 300

# salario = float(input("digite seu salario"))

# if (salario >= 1500 and salario <2000):
#     print(f"seu salario é {salario + 500}")
    
# elif (salario <= 2000):
#     print(f"seu salario é {salario + 400}")

# elif (salario <= 3000):
#     print(f"seu salario é {salario + 300}")

# else:
#     print("você é pobre :")


# Até agora, quando temos um codigo com varias operações sequenciais, é um código estruturado. Se tenho uma ou mais opções é uma estrutura condicional


#temos ainda mais uma estrutura possível, a de repetição. Quando vc tenta cadastrar em um site e nao sabe as políticas de segurança, é possível que vc nao acerte de 1º então vc deve fazer de novo. tudo que é um esforço repetitivo usamos os laços de repetição. 
#temos 2 tipos de laços de repetição, o For e o while. For tenho um numero de vezes que quero algo seja feito, e while quero que execute ate q eu ache o que procuro. 

#SEI QUANTAS VEZES VOU EXECUTAR!

for i in range(1,11):
    print(i)
#com a variavel i entre 1 a 11 (no onze eu paro)
#imprima todo os numeros que estão entre 1 e 11

for dardo in range(1,7):
    print(f"Arremesse o {dardo} º dardo")

#PRECISO QUE ME INFORFE QUANDO PARAR
# exemplo de achar a lapiseira azul na sala
while True:
#enquanto for verdade
    nome = input("Digite um nome (ou 'N' para sair): ")
    #peça um nome ao usuário e armazene na variavel N, ou digitar N 
    if nome.upper() == 'N':
        # se o usuário digitar N
        break
    #pare, se nao volta para o while



















