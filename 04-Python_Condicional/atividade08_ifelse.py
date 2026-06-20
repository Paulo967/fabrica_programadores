#autor Paulo Petrit
#Projeto de condicional if else 

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))   
peso = float(input("digite seu peso: "))
if idade >= 18 and peso < 18.5:
    print(nome, "você está com peso abaixo do normal!")
else:
    print(nome, "você está com peso normal!")