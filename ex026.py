frase=str(input('Digite uma frase qualquer: ')).lower().strip()

print(f'Nesta frase existe {frase.count("a")+1} letras A')
# adicionado mais 1 para a verificação do usuario!

print(f'A primeira vez que aparece e na posição {frase.find("a")}.\nE a ultima vez e na posição {frase.rfind("a")+1}.')


#a função <.find()> procura determinada string da esquerda p direita, a <.rfind()> da direita p esquerda