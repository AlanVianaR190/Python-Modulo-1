
def antPos(n):
    '''
    Mostra o antecessor e o sucessor de um numero
    :param n: numero do tipo inteiro
    :return: o antecessor e o sucessor
    '''
    antecessor = n-1
    sucessor = n+1
    return antecessor, sucessor


n=int(input('Digite um numero: '))
print(antPos(n))

#Esta função \n faz a quebra de linha
print(f'O antecessor desse numero e {n-1}.\nE seu sucessor e {n+1}.')

