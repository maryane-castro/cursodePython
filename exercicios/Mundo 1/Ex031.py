#Desenvolva um programa que pergunte a distancia de uma viagem um Km.
#Calcule o preço da passagem, Cobrando R$0.50 por Km para viagens de até 200km e R$0,45 para viagens mais longas
km = int(input('Qual a diastancia de uma viagem em Km? '))
if km <= 200:
    print('Essa é uma viagem curta de {}Km, e custará R${:.2f}.'.format(km, 0.5*km))
else:
    print('Essa é uma viagem longa de {}Km, e custará R${:.2f}.'.format(km, 0.45*km))