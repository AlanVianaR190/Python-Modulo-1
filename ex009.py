#função
def taboada(n, v=0):

    for c in range(0, v+1):
        print(f"{n} x {c:2} = {n*c}")
    print("FIM")

#programa principal
taboada(4,7)


'''
n=int(input('Digite um numero: '))
print(f'00 x {n} = {n}')
print(f'01 x {n} = {n}')
print(f'02 x {n} = {n*2}')
print(f'03 x {n} = {n*3}')
print(f'04 x {n} = {n*4}')
print(f'05 x {n} = {n*5}')
print(f'06 x {n} = {n*6}')
print(f'07 x {n} = {n*7}')
print(f'08 x {n} = {n*8}')
print(f'09 x {n} = {n*9}')
print(f'10 x {n} = {n*10}')
print('---'*10)

#Usando laço for
for q in range(0,11):
    #Formatado a quantidade de largura
    print(f'{q:2} x {n} = {n * q}')'''
