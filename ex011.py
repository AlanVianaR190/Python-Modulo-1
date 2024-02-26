#biblioteca math
import math

alt=float(input('Digite a altura da parede: '))
larg=float(input('Digite a largura da parede: '))
area1=alt*larg

print(f'A area da parede e equivalente a {area1:.2f}m')

#Usando a função <math.ceil> da biblioteca math para arredondar o valor
print(f'A quantidade de tinta necessaria para pintar e de {math.ceil(area1/2):.0f} lts')

#
quanTint = lambda x, y: f"{math.ceil((x * y) / 2):.0f}"
print(f'A quantidade de tinta necessaria para pintar e de {quanTint(alt,larg)} lts')

