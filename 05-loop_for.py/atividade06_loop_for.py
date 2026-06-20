# autor Paulo petrit
# Projeto de loop for

nota = [int(input("Digite uma nota: ")) for _ in range(4)]
media = (nota[0] + nota[1] + nota[2] + nota[3]) / 4
print(f"A média das notas é: {media}")
