#recebendo input
nome = input("Qual é seu nome?:")
idade = input("Qual sua idade?:")
# fstring aceita variaveis
print(f"Olá {nome}! você tem {idade} anos")
#input é sempre string precisamos transformar em inteiro
idade=int(idade)
# condição para 3 respostas diferentes
if idade >= 60:
    print("Você é maior de idade e idoso")
elif idade >=18:
    print ("Você é maior de idade")
else:
    print("Você é menor de idade")

#exemplo d loop for
nomes = ["Edney", "Ana", "João"]

for nome in nomes:
    print(nome)