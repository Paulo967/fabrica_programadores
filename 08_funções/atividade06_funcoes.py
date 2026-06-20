


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


#Função calcular - 4 operações matematicas
def calcular(valor1, valor2):
    somar = valor1 + valor2
    subtrair = valor1 - valor2
    multiplicar = valor1 * valor2
    dividir = valor1 / valor2

    print(f"A soma é: {somar}")
    print(f"A subtração é: {subtrair}")     
    print(f"A multiplicação é: {multiplicar}")
    print(f"A divisão é: {dividir}")
    
  
#chamada da função
calcular(valor1, valor2)

    