#Joquempo
from random import choice
ppt = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(ppt)
play = str(input('Escolha "Pedra", "Papel", ou "Tesoura":  ')).upper()
if play in ppt:
    if comp == play:
        print('Oops, nós dois escolhemos {}.'.format(comp))
    elif (comp == 'PEDRA' and play == 'TESOURA') or (comp == 'TESOURA' and play == 'PAPEL') or (comp == 'PAPEL' and play == 'PEDRA'):
        print('HAA! TE GANHEI! {} ganha de {}.'.format(comp, play))
    else:
        print('Ahhh voce me ganhou. {} ganha de {}.'.format(play, comp))
else:
    print('ERRO! Digite uma opção valida.')