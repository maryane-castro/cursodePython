'''Faça um programa que tenha uma função chamada maior(), que receba vários 
parametros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer qual deles é maior.'''
from time import sleep

def maior(*num):
    print('-='* 30,'\nAnalizando os valores passados...')
    for x in num:
        print(x, end=' ', flush=True)
        sleep(0.1)
    if len(num) > 0:
        maior = max(num)
    else:
        maior = 0
    print(f'Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {maior}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()