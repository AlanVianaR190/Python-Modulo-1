a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))
c=int(input("Digite o terceiro numero: "))

#pegar o menor
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

#pegar o maior
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print(f"O maior valor e {maior}.",end=" ")
print(f"O menor valor e {menor}.")



