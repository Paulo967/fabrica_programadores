# autor: Paulo petrit
# Projeto de condicional if else

# Declaração de variáveis
nome= input("digite seu nome: ")
nota = float(input("digite sua nota: "))
#condicional if else
if nota >= 7:
    print(nome, "você foi aprovado!")
elif nota <= 5:
    print(nome, "você está de recuperação!")   
else:
    print(nome, "você foi reprovado!")
