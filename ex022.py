nome=str(input('Digite um nome: '))

#A função <.upper> deixa as letras maiusculas
print(f'O nome {nome} com todas as letras maiusculas fica assim {nome.upper()}')

#A função <.lower> deixa as letras minusculas
print(f'E com todas as letras minusculas fica assim {nome.lower()}')

#A função <.count> mostra a quantidade
print(f'O nome tem ao todo {len(nome) - nome.count(" ")}')

#A função <.split> para dividir a partir dos espaços
cortes=nome.split()
print(f'O primeiro nome {cortes[0]} tem ao todo {len(cortes[0])}')
