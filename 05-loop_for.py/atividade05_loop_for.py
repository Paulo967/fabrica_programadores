# Autor Paulo Petrtit
# Projeto de loop for   

numeros = [int(input("Digite um número: ")) for _ in range(10)]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)