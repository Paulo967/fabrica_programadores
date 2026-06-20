# autor Paulo Petrit
# Projeto de condicional if else

nome = input("digite seu nome: ")
idade = float(input("digite sua idade: "))
preço = float(input("digite o preço do produto: "))
if idade >= 18 and preço >= 100:
    print(nome, "o produto está caro para você!")
else:
    print(nome, "o produto está barato para você!")