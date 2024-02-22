#função
def bemVindo(n):
    return f"E um prazer conhece-lo {n}"


n="Alan"
bemVindo(n)

nome=input('Digite seu nome: ')

#saida no formato do livro
print('E um prazer te conhecer, %s!'% (nome))

print('---'*10)

#saida no formato do curso em video
print('E um prazer conhece-lo, {}!'.format(nome))

print('---'*10)

#saida no formato FMU
print(f'E um prazer te conhecer, {nome}!')

#formatando o espacamento da saida

#alinhamento centralizado
print('Prazer em conhece-lo {:^10}!'.format(nome))

#alinhamento centralizado com simbolos
print('Prazer em conhece-lo {:-^10}!'.format(nome))
