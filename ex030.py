num=int(input("Digite um numero para saber se ele e par ou impar: "))

#Condição para verificar se e par
if num%2==0:
    print("Este e um numero par!")
else:
    print("Este e um numero impar!")

#
imPar = lambda x: "Par" if x % 2 == 0 else "Impar"
print(imPar(num))


