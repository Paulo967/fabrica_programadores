#autor: Paulo Petrit
# Projeto de Funções

# Declaração de variáveis
def renda(nome, salario):
    if salario >= 1000:
        print(nome, "boa renda")
    elif salario >= 700:
        print(nome, "renda razoável")
    elif salario >= 500:
        print(nome, "renda baixa")
    else:
        print(nome, "renda muito baixa")

nome = input("Nome: ")
salario = float(input("Salário: "))

renda(nome, salario)
