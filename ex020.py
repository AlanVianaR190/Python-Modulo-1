import random
n1=str(input('Digite o nome do primeiro aluno: '))
n2=str(input('Digite o nome do segundo aluno: '))
n3=str(input('Digite o nome do terceiro aluno: '))
n4=str(input('Digite o nome do quarto aluno: '))

nomes=[n1,n2,n3,n4]

#A função <shuffle> do modulo <random> sorteia a ordem
random.shuffle(nomes)

print('A ordem de apresentação e:')
print(nomes)
