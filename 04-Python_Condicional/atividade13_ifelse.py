nome = input('escreva seu nome: ')
peso = float(input('escreva seu peso: '))
altura = float(input('escreva sua altura: '))
imc = peso / (altura ** 2)  
if imc < 18.5:
    print(nome, "você está abaixo do peso!")
elif imc < 24.9:
    print(nome, "você está com peso normal!")
elif imc < 29.9:
    print(nome, "você está com sobrepeso!")
elif imc < 34.9:
    print(nome, "você está com obesidade grau 1!")
elif imc < 39.9:
    print(nome, "você está com obesidade grau 2!")
else:
    print(nome, "você está com obesidade grau 3!")   