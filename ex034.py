sal=float(input("Digite o salario do funcionario: R$"))

#
if sal>1250.00:
    aumento=sal*0.10
else:
    aumento=sal*0.15

print(f"O aumento do salario e de R${aumento:.2f}.\nO total e de R${sal+aumento:.2f}")

#
aument = lambda x: x * 0.10 if x > 1250.00 else x * 0.15
print(f"O aumento do salario e de R${sal:.2f}. O total e de R${sal + aument(sal):.2f}")