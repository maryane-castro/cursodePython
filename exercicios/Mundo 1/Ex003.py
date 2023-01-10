#crie um programa que leia dois numeros e mostre a soma entre eles

n1 = int(input('Digite um numero:  '))
n2 = int(input('Digite outro numero:  '))
l = '\033[m'
a = '\033[4;34m'
soma = n1 + n2
print('A soma de {}{} e {}{} é \033[1;31m{}{}.'.format(a, n1, n2, l, soma, l))
