#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos numeros
# [ 5 ] Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
menu = 4
enfeite = '-=' * 20
while menu != 5:
    if menu == 4:
        n1 = int(input('Digite um numero:  '))
        n2 = int(input('Digite outro numero:  '))
    menu = int(input('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa
Escolha uma opção:  '''))
    if menu < 1 or menu > 5:
        print('Erro! Escolha uma das opções entre 1 e 5.')
    else:
        print(enfeite,'\033[1;33m')
        if menu == 1:
            print('A soma entre {} e {} é {}.'.format(n1 , n2 , n1+n2))
        if menu == 2:
            print('O produto de {} e {} é {}.'.format(n1 , n2 , n1*n2))
        if menu == 3:
            if n1 > n2:
                print('O numero maior é o {}.'.format(n1))
            elif n1 < n2:
                print('O numero maior é o {}.'.format(n2))
            else:
                print('Os dois numeros digitados são iguais.')
        if menu == 5:
            print('SAINDO DO PROGRAMA...')
        print('\033[m'+enfeite)