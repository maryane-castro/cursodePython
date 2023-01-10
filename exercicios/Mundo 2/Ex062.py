#Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele diser que quer mostrar 0 termos. 
num = int(input('Digite um numero:  '))
raz = int(input('Digite a razão da P.A.:  '))
qts = 10
while qts != 0:
    c = 0
    while c != qts:
        print(num, '-> ', end='')
        num += raz
        c += 1
    qts = int(input('Mostrar mais quantos? '))
print('ACABOU!')
    