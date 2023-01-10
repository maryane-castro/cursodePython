#Faça um programa que leia um ano qualquer e mostre se ele é bisexto
from datetime import date
ano = int(input('Digite um ano. Coloque 0 para analizar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto.'.format(ano))
else:
    print('O ano {} NÃO é bisexto.'.format(ano))

'''if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bisexto.'.format(ano))
        else:
            print('O ano {} NÃO é bisexto.'.format(ano))
    else:
        print('O ano {} é bisexto.'.format(ano))
else:
    print('O ano {} NÃO é bisexto.'.format(ano))'''