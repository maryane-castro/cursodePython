#crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos Dolares ela pode comprar.
#Considere: US$1,00 = R$3,27
cart = float(input('Quanto dinheiro tem na sua carteira?  '))
dol = cart / 5.67
print('Você pode comprar \033[1;32mUS${:.2f}\033[m com \033[1;32mR${:.2f}\033[m'.format(dol, cart))