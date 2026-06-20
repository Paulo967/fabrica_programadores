# autor: Paulo petrit

# Projeto de Funções

# Declaração de variáveis
def verificar_nota(nome, nota):
    if nota >= 7:
        print(nome, "você foi aprovado!")
    else:
        print(nome, "você foi reprovado!")


nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

verificar_nota(nome, nota)