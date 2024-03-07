a=float(input("Digite o primeiro comprimento da reta: "))
b=float(input("Digite o segundo comprimento da reta: "))
c=float(input("Digite o terceiro comprimento da reta: "))

#
if a+b>c and a+c>b and b+c>a:
    print("\033[92mE possivel fazer um triangulo!\033[0m")
else:
    print("\033[91mNão e possivel formar um triangulo!\033[0m")