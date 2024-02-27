n1= int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))

#recomendado criar uma variavel para a saida se no caso utiliza-la mais de uma vez
s=n1+n2
print('---'*10)

#saida utilizando uma variavel para o resultado
print(f'A soma de {n1} com {n2} tem o resultado {s}!')

#saida não utilizando variavel
print(f'A soma de {n1} com {n2} tem o resultado {n1+n2}!')

#
soma = lambda x, y, z: x + y + z

x1=int(input("Digite um numero: "))
x2=int(input("Digite um numero: "))
x3=int(input("Digite um numero: "))

print(soma(x1,x2,x3))
