#função
def media(*n):

    soma=sum(n)
    quant=len(n)
    media=soma/quant
    return media


#programa principal
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))

medi=(n1+n2)/2

print(f'A media da nota e: {medi:.1f}')

print(media(n1,n2))
