from math import hypot
cat_op=float(input('Digite o valor do cateto oposto: '))
cat_ad=float(input('Digite o valor do cateto adjascente: '))
hipo=hypot(cat_op,cat_ad)

#Usando a variavel <hipo(a,b)>
print(f'O comprimento da Hipotenusa e de: {hipo:.2f}')

#
hipo1 = lambda x, y: f'O comprimento da Hipotenusa de é: {hypot(x, y):.2f}'
hipotenusa = hipo1(5,5)
print(hipotenusa)



