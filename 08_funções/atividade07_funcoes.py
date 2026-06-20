#autor Paulo Petrit
#Projeto de condicional if else 
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = calcular_imc(peso, altura)

if imc < 18.5:
    print(nome, "você está abaixo do peso ideal. Seu IMC é:", round(imc, 2))
else:
    print(nome, "você está com peso normal. Seu IMC é:", round(imc, 2))