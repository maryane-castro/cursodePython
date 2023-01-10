#Faça um programa que ajude um jogador da MEGASENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 
# 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = int(input('Quantos jogos você quer que eu sorteie?  '))
lista = []
data = []
print(f'-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')
for x in range(0, jogos+1):
    while len(data) < 6:
        num = randint(1, 60)
        if num not in data:
            data.append(num)
    lista.append(sorted(data[:]))
    data.clear()
for c in range(1, len(lista)):
    sleep(1.0)
    print(f'Jogo {c}: {lista[c-1]}')
print('-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-')
