#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se ja passou do tempo do alistamento
# seu programa tambem devera mostrar o tempo que falta ou passou do prazo 
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento do jovem?  '))
if nasc == atual - 18:
    print('Esse é o ano do seu alistamento.')
elif nasc > atual:
    print('Voce nem nasceu ainda o mentiroso, mas seu alistamento será em {}.'.format(nasc + 18))
elif nasc > atual - 18:# se o ano de nascença foi depois de 2003
    print('Seu alistamento será daqui a {} anos(s)'.format(nasc + 18 - atual))
else:
    print('O ano de seu alistamento foi a {} ano(s) atras!'.format(atual - (nasc + 18)))