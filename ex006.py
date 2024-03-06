n = int(input('Digite um numero: '))

print(f'O dobro desse numero e {n*2}')
print(f'O triplo desse numero e {n*3}')

print('---'*10)

#Formatado a quantidade de numeros a partir de dois digitos depois do ponto
print(f'A raiz quadrada desse numero e {n**(1/2):.2f}.', end=' ')

#Esta função <end=' '> faz a junção com alinha de baixo
raizCub = n**(1/3)
print(f'A raiz cubica desse numero e {raizCub:.2f}.')
