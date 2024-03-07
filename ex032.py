from datetime import date

ano=int(input("Digite o ano para saber se e bissexto ou não (coloque 0 para analisar o ano atual): "))

if ano==0:
    #A função <.today().year> utiliza o ano registrado na maquina
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f"O ano de {ano} bissexto!")
else:
    print(f"O ano de {ano} não e bissexto!")









