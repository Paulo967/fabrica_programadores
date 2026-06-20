# autor Paulo petrit
# Projeto de loop while 

numero = int(input("digite um numero para ver a tabuada:"))
i = int(input("Digite quanto começar a tabuada: "))
f = int(input("Digite até onde a tabuada deve ir: "))     
while i <= f:
    print(f"{numero} x {i} = {numero * i}")
    i += 1   
