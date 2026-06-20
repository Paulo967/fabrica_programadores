#autor paulo Petrit
#Projeto de condicional if else

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
voce = input("você possui carteira de motorista? (sim/não): ")
if "sim" in voce.lower():
    print(nome, "você é elegível para dirigir!")
else:
    print(nome, "você não é elegível para dirigir!")