#função
def soma(*n):
    '''
    :param n: pode inserir varios valores no parametro
    :return: o total da soma
    '''
    total=sum(n)

    return total

n1=int(input("Digite um numero: "))
n2=int(input("Digite um numero: "))
n3=int(input("Digite um numero: "))

#print(soma(3, 4, 10))
print(soma(n1,n2,n3))

'''n1= int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))

#recomendado criar uma variavel para a saida se no caso utiliza-la mais de uma vez
s=n1+n2
print('---'*10)

#saida utilizando uma variavel para o resultado
print(f'A soma de {n1} com {n2} tem o resultado {s}!')

#saida não utilizando variavel
print(f'A soma de {n1} com {n2} tem o resultado {n1+n2}!')'''
