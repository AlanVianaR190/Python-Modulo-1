'''numero = int(input("Digite um número de 0 a 9999: "))

# Obtém o dígito da unidade
unidade = numero % 10

# Remove o dígito da unidade do número
numero = numero // 10

# Obtém o dígito da dezena
dezena = numero % 10

# Remove o dígito da dezena do número
numero = numero // 10

# Obtém o dígito da centena
centena = numero % 10

# Remove o dígito da centena do número
numero = numero // 10

# Obtém o dígito do milhar
milhar = numero % 10

# Imprime os dígitos separados
print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)'''

numero = int(input("Digite um número de 0 a 9999: "))

# Converte o número para uma string
numero_str = str(numero)

# Completa a string com zeros à esquerda se necessário
numero_str = numero_str.zfill(4)

# Imprime cada dígito separadamente
print("Milhar:", numero_str[0])
print("Centena:", numero_str[1])
print("Dezena:", numero_str[2])
print("Unidade:", numero_str[3])


