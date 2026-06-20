# autor: Paulo Petrit
# Projeto: Empréstimo Bolos de Pote 

def calcular_emprestimo(valor, taxa, meses):

    montante = valor * ((1 + taxa) ** meses)
    juros = montante - valor

    print("\n--- Resultado do empréstimo ---")
    print("Valor emprestado: R$", valor)
    print("Valor dos juros: R$", round(juros, 2))
    print("Valor total a pagar: R$", round(montante, 2))

    limite = valor * 0.10

    if juros <= limite:
        print("Empréstimo aprovado!")
    else:
        print("Empréstimo não aprovado!")
        print("Os juros ultrapassam 10% do valor emprestado.")



# Dados do empréstimo

valor = 20000
taxa = 0.0125  # 1,25% ao mês

meses = int(input("Digite a quantidade de meses para parcelar: "))


calcular_emprestimo(valor, taxa, meses)