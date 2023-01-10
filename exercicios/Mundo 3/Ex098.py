'''Faça um programa que tenha uma função chamada contador(), que receba tres
 parametros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar tres contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada'''

from time import sleep

def contador(i, f, p=1):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    '''
    if p == 0:
        p = 1
    if f < i:
        nf = f - 1
        if p > 0:
            p = -p
    elif f > i:
        nf = f + 1
        if p < 0:
            p = -p
    print('-='* 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for x in range(i,nf,p):
        print(x, end=' ', flush= True)
        sleep(0.5)
    print('FIM!')


contador(1, 10, -1)
contador(10, 0, 2)
print('-='*30,'\nAgora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio:  '))
fim = int(input('Fim:  '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)