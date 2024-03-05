import math
#Importando diretamente da biblioteca math. o seno, tangente e cosseno
from math import sin,tan,cos

ang=float(input('Digite o angulo aqui: '))
print(f'O Seno deste angulo e de {sin(math.radians(ang)):.2f}')
print(f'A Tangente deste angulo e de {tan(math.radians(ang)):.2f}')
print(f'O Cosseno deste angulo e de {cos(math.radians(ang)):.2f}')
