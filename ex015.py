#
km=float(input('Digite a quantidade de kilometros percoridos: '))
dia=int(input('Digite aqui a quantidade de dias: '))
preco=(60.0*dia)+(0.15*km)
print(f'O valor a ser pago pelo aluguel do carro e de R${preco:.2f}')

#
km1=float(input('Digite a quantidade de kilometros percoridos: '))
dia1=int(input('Digite aqui a quantidade de dias: '))
novoPreco = lambda kms, dias: (60.0 * dias) + (0.15 * kms)
print(f'O valor a ser pago pelo aluguel do carro e de R${novoPreco(km1,dia1):.2f}')
