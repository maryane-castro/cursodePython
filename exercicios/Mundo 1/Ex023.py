#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
num = int(input('Digite um numero de 0 a 9999:  '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Unidade:', uni)
print('Dezena: ', dez)
print('Centena:', cen)
print('Milhar: ', mil)