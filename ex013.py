#
sal=float(input('Digite aqui o salario: R$'))
print(f'O novo salario com o aumento de 15% e R${sal+(sal*0.15):.2f}')

#
novoSal = lambda x: x + (x * 0.15)
antigoSal = float(input('Digite aqui o salario: R$'))
print(f'O novo salario com o aumento de 15% e R${novoSal(antigoSal):.2f}')
