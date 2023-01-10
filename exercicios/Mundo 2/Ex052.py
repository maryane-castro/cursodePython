#Faça um programa que leia um numero e diga se ele é primo ou não
num = int(input('Digite um numero para saber se ele é primo:  '))
resp = 0
for div in range(2 ,num):
    if num % div == 0:
        resp = 1
if resp == 1:
    print('O numero {} NÃO é primo!'.format(num))
elif resp == 0:
    print('O numero {} É primo!'.format(num))
'''
for num in range(1, 100):
    resp = 0
    for div in range(2 ,num):
        if num % div == 0:
            resp = 1
    if resp == 0:
        print(num)'''# Da pra usar esse pra descobrir os numeros primos de um intervalo entre dois numeros