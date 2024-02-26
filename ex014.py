#
grau=float(input('Digite aqui a temperatura em graus celsius: '))
print(f'A temperatura {grau}ºC e equivalente a {(grau*1.8)+32:.1f}ºF')

#
temp = float(input('Digite aqui a temperatura em graus celsius: '))
grau1 = lambda x: (x * 1.8) + 32
print(f'A temperatura {temp}ºC e equivalente a {grau1(temp):.1f}ºF')
