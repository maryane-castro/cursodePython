#Refaça o desafio 51, lendo o primeiro termo e a razão de uma pa,
#mostrando o 10 primeiros termos da progressão aritmetica usando a estrutura while
pa = int(input('Digite o primeiro termo da P.A.:  '))
razao = int(input('Digite a razão da P.A.:  '))
c = 0
while c < 10:
    print(pa, '->',end=' ')
    pa += razao
    c += 1
print('ACABOU')

    