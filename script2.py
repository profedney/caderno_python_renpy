# Atividade 02 - python

"""
programador: Prof. Edney Rossi

programa para testar várias funções em python

"""

# O bloco a seguir testa uma condição usando a instrução `if-else`:
if 10 > 1:
    # Se a condição (10 > 1) for verdadeira, imprime esta mensagem:
    print("Condição VERDADEIRA")
else:
    # Caso contrário, imprime esta mensagem:
    print("condição FALSA")

# Aqui, o código demonstra diferentes tipos de variáveis:
x = str(3)    # Converte o número 3 para uma string e armazena em 'x'
y = int(3)    # Converte o número 3 para um inteiro e armazena em 'y'
z = float(3)  # Converte o número 3 para um float (ponto flutuante) e armazena em 'z'

# Imprime o valor das variáveis x, y e z
print(x)
print(y)
print(z)

# Imprime o tipo de cada variável usando a função `type()`
print(type(x))  # <class 'str'>, pois x é uma string
print(type(y))  # <class 'int'>, pois y é um inteiro
print(type(z))  # <class 'float'>, pois z é um float

# Cria uma lista de frutas e desempacota em três variáveis
frutas = ["banana", "maçã", "mamão"]
a, b, c = frutas  # A lista é dividida em três partes e atribuída a a, b e c

# Imprime cada uma das variáveis
print(a)  # Imprime 'banana'
print(b)  # Imprime 'maçã'
print(c)  # Imprime 'mamão'

# Imprime as variáveis separadas por espaço
print(a, b, c)  # Imprime 'banana maçã mamão'

# Tenta somar as variáveis a, b e c. Como são strings, isso concatenará os valores
print(a + b + c)  # Imprime 'banana maçã mamão'

# Imprime uma mensagem de término do programa
print("fim do programa")

# Cria duas variáveis numéricas e imprime a soma delas
num1 = 5
num2 = 6
print(num1 + num2)  # Imprime 11, a soma dos números 5 e 6

# Cria duas variáveis de texto e imprime a concatenação delas
texto1 = "5"
texto2 = "6"
print(texto1 + texto2)  # Imprime '56', a concatenação das strings '5' e '6'
