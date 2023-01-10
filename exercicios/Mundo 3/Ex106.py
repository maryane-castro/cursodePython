'''Faça um mini-sistema que utiliza o interactive help do Python. O usuario vai 
digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra FIM, 
o programa se encerrará
Obs: Use cores'''

from time import sleep

def titulo(tit, cor):
    print(cor)
    print('~' * (len(tit) + 4))
    print(f'  {tit}  ')
    print('~' * (len(tit) + 4), '\033[m')
def ajuda(resp):
    titulo(f'Acessando o manual do comando "{resp}".', cor= '\033[1;44m')
    print('\033[30;47m')
    print(eval(resp).__doc__, '\033[m')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', '\033[1;42m')
    duv = str(input('Função ou biblioteca > '))
    if duv.upper() == 'FIM':
        titulo('ATÉ LOGO!', '\033[1;41m')
        break
    ajuda(duv)
