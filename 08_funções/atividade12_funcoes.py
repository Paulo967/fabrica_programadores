# autor Paulo Petrit
# Projeto: listas

def mostrar_jogadores(nomes):
    print("---Maiores jogadores de futebol da história---")
    print(f'1° {nomes[0]}')
    print(f'2° {nomes[1]}')
    print(f'3° {nomes[2]}')
    print(f'4° {nomes[3]}')
    print(f'5° {nomes[4]}')
    print(f'6° {nomes[5]}')


nomes = ['Pelé', 'Neymar', 'Ronaldo', 'Ronaldinho', 'Zico', 'Garrincha']
def remover_paises():
    penta = ["brasil", "Paraguai", "Chile"]

    print(penta)
    penta.pop(2)
    print(penta)

    print(penta)
    penta.pop()
    print(penta)


remover_paises()
mostrar_jogadores(nomes)

