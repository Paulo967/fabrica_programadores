nome = input('escreva seu nome: ')
idade = int(input('escreva sua idade: '))
Cnh = input('você possui carteira de motorista? (sim/não): ')
if idade >= 18:
    if "sim" in Cnh.lower():
        print(nome, "você pode dirigir!")
elif idade < 18:
    print(nome, "você é menor de idade")
else:   print(nome, "você não pode dirigir!")