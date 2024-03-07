from time import sleep

km=int(input("Digite a distancia em km da viagem para calcular o valor: "))
print("Aguarde..."),sleep(1)

#
if km<=200:
    valor=km*0.50
else:
    valor=km*0.45

print(f"Sua viagem de {km}km ira custar R${valor:.2f}")

#
kms = lambda x: x * 0.50 if x <= 200 else x * 0.45
print(f"Sua viagem de {km}km ira custar R${kms(km):.2f}")
