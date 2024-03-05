from random import choice
n1=str(input('Digite o nome do primeiro aluno: '))
n2=str(input('Digite o nome do segundo aluno: '))
n3=str(input('Digite o nome do terceiro aluno: '))
n4=str(input('Digite o nome do quarto aluno: '))

nomes=[n1,n2,n3,n4]

#Função <choice()> para sortear um nome
print(f'O nome sorteado foi {choice(nomes)}')
