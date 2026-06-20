# autor Paulo Petrit
# Projeto de loop for

numero = int(input("usuario, digite um número para ver a tabuada: "))

comeco = int(input("Digite quanto começar a tabuada: "))
fim = int(input("Digite até onde a tabuada deve ir: "))

for i in range (comeco, fim + 1):
    print(f" {numero} x {i} = {numero * i}")