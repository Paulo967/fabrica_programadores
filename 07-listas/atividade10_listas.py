#autor paulo petrit
# Projeto: listas
# Programa cadastro-FABPROG 

#listas     0          1            2         
nomes = ['Pelé', 'neymar', 'Ronaldo']
# Adicionando um item em uma lista
nomes.append('Ronaldinho')
print(nomes)
#excluindo dados com pop em branco
print(nomes)
nomes.remove('neymar')
print(nomes)
novo_nome = input('Digite o nome do jogador: ')
nomes.append(novo_nome)
print(nomes)
