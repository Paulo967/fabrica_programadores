nome = input('escreva seu nome: ')
nota1 = float(input('escreva sua nota: '))
nota2 = float(input('escreva sua nota: '))
nota3 = float(input('escreva sua nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(nome, "você foi aprovado!")
elif media >= 5 and media < 7:
    print(nome, "você está de recuperação!")    
else:
    print(nome, "você foi reprovado!")
