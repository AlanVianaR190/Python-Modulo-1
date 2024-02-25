def medidas(k):
    metr=m*10
    cent=m*100
    mili=m*1000
    return f"{k}km = {metr}m = {cent}cm = {mili}mm"


m=float(input('Digite a distancia em kilometros: '))
print(medidas(m))

print(f'Esta distancia em centimetros e equivalente a {m*100}cm',end=' ')
print(f',e em milimitros e equivalente a {m*1000}mm')
