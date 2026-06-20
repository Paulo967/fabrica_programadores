nome = input('escreva seu nome: ')
telefone = input('escreva seu telefone: ')
cidade = input('escreva sua cidade: ')
salario = float(input('escreva seu salário: '))
if salario >= 1000:
    print(nome, "você possui uma boa renda!")
elif salario >= 700 and salario < 1000:
    print(nome, "você possui uma renda razoável!")
elif salario >= 500 and salario < 700:
    print(nome, "você possui uma renda baixa!")
else:
    print(nome, "você possui uma renda muito baixa!")
