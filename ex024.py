#a função <.strip> tira os espaços vazio no começo e no fim
cidade=str(input('Digite o nome de uma cidade: ')).upper().strip()

print(f'Esta cidade começa com a palavra SANTO: {"SANTO" in cidade[0:5]} ')
#print(f'Esta cidade começa com a palavra SANTO: {cidade[0:5] == "SANTO"}')
