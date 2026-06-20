# autor Paulo petrit
# Projeto de loop while
i = 1

nota = int(input("Digite uma nota: "))
while nota < 0 or nota > 10:
    nota = int(input("Digite uma nota: "))
print(f"A nota digitada é: {nota}")
