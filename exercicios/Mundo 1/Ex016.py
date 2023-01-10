#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor
num = float(input('Digite um numero:  '))
print('A porção inteira do numero digitado é {}.'.format(floor(num)))