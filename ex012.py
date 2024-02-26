#
val=float(input('Digite o valor do produto: R$'))
novoVal=val-val*0.37
print(f'O valor do produto com o desconto de 37.50% e de R${novoVal:.2f}')

#
val2 = float(input('Digite o valor do produto: R$'))
novoVal2 = lambda x: f"{x - x * 0.37:.2f}"
print(f'O valor do produto com o desconto de 37.50% e de R${novoVal2(val2):.2f}')
