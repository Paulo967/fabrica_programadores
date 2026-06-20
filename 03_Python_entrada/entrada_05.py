#autor: Paulo petrit
#Projeto entrada com input e f-string

#Declaração de variáveis
nome = input("digite seu nome: ")
valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = valor1 + valor2
subtração = valor1 - valor2
multiplicação = valor1 * valor2
divisão = valor1 / valor2
#exibir resultados com F-string
print(f"Nome: {nome}")
print(f"A soma é: {soma}")
print(f"A subtração é: {subtração}")
print(f"A multiplicação é: {multiplicação}")
print(f"A divisão é: {divisão}")
