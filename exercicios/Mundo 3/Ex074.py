#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e
# tambem indique o menos e o maior valor que estão na tupla. 
from random import randint
tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados: ', end= '')
for cont in tup:
    print(cont, end=' ')
print(f'\nO maior valor sorteado foi {max(tup)}.')#Método max pega o maior valor da tupla
print(f'O menor valor sorteado foi {min(tup)}.')#Método min pega o menor valor da tupla


'''
print(f'\nO maior valor sorteado foi {sorted(tup)[-1]}.')
print(f'O menor valor sorteado foi {sorted(tup)[0]}.')'''