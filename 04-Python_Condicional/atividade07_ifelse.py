#autor Paulo Petrit
#Projeto de condicional if else

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
Produto = float(input("digite o preço do produto: "))

if Produto >= 100:
    preco_final = Produto - (Produto * 0.10)
else:
    preco_final = Produto - (Produto * 0.05)


    print(nome, "o preço final do produto é:", preco_final)
