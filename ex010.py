#
real=float(input('Digite o valor que esta na sua carteira: R$'))
converMoeda = lambda x: f"{x * 0.20:.2f}"
print(f"R${real} e equivalente a {converMoeda(real)}")

#
dol=real*0.20
print(f'A quantia de R${real:.2f}(reais) que esta na sua carteira e equivalente a U${dol:.2f}(dolares)')
print('Na epoca do curso...',end=' ')
print(f'R${real:.2f}(reais) e equivalente a U${real/3.27:.2f}(dolares)')
