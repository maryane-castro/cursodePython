'''Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e 
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep

def sorteia(lis1):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(5):
        x += 1 #pra parar de avisar q não usei o x
        lis1.append(randint(0,9))
        print(lis1[-1], end=' ', flush= True)
        sleep(0.5)
    print('PRONTO!') 
def somaPar(lis2):
    soma = 0
    for x in lis2:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {lis2}, temos {soma}.')

#Programa principal
lista = []
sorteia(lista)
somaPar(lista)