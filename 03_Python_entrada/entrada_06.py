#autor: Paulo petrit
#Projeto IMC com input e f-string

#Declaração de variáveis
peso = float(input("digite seu peso (kg): "))
altura = float(input("digite sua altura (m): "))
imc = peso / (altura * 2)

#exibir resultado
print(f"Seu IMC é: {imc:.2f}")