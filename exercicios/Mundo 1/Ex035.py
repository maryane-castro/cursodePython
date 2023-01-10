#Desenvolva um programa que leia o comprimento de tres retas e
#  diga ao usuario se elas podem ou não formar um triangulo.
a = float(input('Reta numero 1:  '))
b = float(input('Reta numero 2:  '))
c = float(input('Reta numero 3:  '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triangulo.')
else: 
    print('As retas NÃO podem formar um triangulo.')

'''if (b - c)< a < b + c:
    if (a - c) < b < a + c:
        if (a - b) < c < a + b:
            print('As retas PODEM serem usadas para formar um triangulo.')
        else: print('As retas NÃO podem serem usadas para formar um triangulo.')
    else: print('As retas NÃO podem serem usadas para formar um triangulo.')
else: print('As retas NÃO podem serem usadas para formar um triangulo.')'''
    