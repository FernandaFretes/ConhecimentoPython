#Algoritmo -> sequencia de passos para executar uma tarefa!

#3 estruturas possiveis no algoritmo

#1 - Estrutural (Sequencia de passos contínuos)
#2 - Condicional (DECISAO - Vou executar um script se acontecer X e outro se Y)
#3 - Repetição - permite executar varias vezes o mesmo codigo

#variaveis
#espaços de memória que pode armazenar dados para a execução de um processo!

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

# #para converar com o usuário eu uso o input
# altura = float(input("Digite sua altura"))
# #a variavel altura recebe um valor quebrado de altura

# print("sua altura é ")
# #exibe para mim a "FORMATAÇÃO" do texto com o valor de uma variavel

# nome = input("Digite seu nome ")
# sobrenome = input("Digite seu sobrenome")
# print(nome + sobrenome)


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

salario = float(input("digite seu salario"))

if (salario <= 1500):
    print(f"seu salario é {salario + 500}")
    
elif (salario <= 2000):
    print(f"seu salario é {salario + 400}")

elif (salario <= 3000):
    print(f"seu salario é {salario + 300}")

else:
    print("você é pobre :(")







