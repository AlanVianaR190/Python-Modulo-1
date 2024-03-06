from random import randint
from time import sleep

print("Advinhe o numero em que estou pensando!"),sleep(2)
numero=int(input("Digite um numero de 1 a 5: "))

#A função <sleep()> para a mquina dar uma pausa de 2 segundos antes de prosseguir
print("Pensando..."),sleep(2)

#A função <randint()> para maquina sortear numero aleatorio de 1 ate 5
maquina=randint(1,5)

if numero == maquina:
    print("Acertou")
else:
    print("Errou")

print(f"Estava pensando em {maquina}!")


#
maquina1 = lambda x: "Acertou" if x == randint(1, 10) else f"Errou, pensava em {randint(1, 10)}"
num = int(input("Digite um numero: "))
print(maquina1(num))