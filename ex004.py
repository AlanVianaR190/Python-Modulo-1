#como o tipo primitivo não esta identificado antes do input toda saida de dado será string(str)
n=input('Digite um numero ou uma letra:')
print(type(n))

#a função .isnumeric identifica se e possivel converter o dado da saida em numero
print('Pode ser do tipo numerico:',n.isnumeric())

print('---'*10)

#a função .isalpha identifica se e possivel converter o dado da saida em letra
print(f'Pode ser do tipo alfabetico: {n.isalpha()}')

#estas funções sao chamadas de metodos de tipagem