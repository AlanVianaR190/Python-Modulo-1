from math import ceil
num=float(input('Digite um numero real: '))

#Usando o tipo <int()> para formatar a variavel do tipo float
print(f'Este numero {num}.\nRepresentado de forma inteira é de {int(num)}.',end=' ')

##Usando a função <ceil()> para arredondar o valor da variavel
print(f'Este numero com valor arredondado e de {ceil(num)}')


