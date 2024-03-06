import time

vel=int(input("Digite a velocidade do veiculo em km: "))
print("Processando..."),time.sleep(2)

#
if vel>80:
    print(f"A velocidade do veiculo de {vel}km/h ultrapassa o limite de 80km/h")
    print(f"Multa de R${(vel-80)*7:.2f}")

print("Pode seguir e dirija com segurança!")