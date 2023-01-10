#Crie um programa que cria uma matriz de dimenção 3X3 3 preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[],[],[]] 
for linha in range(0,3):
    for item in range(0,3):
        matriz[linha].insert(item, int(input(f'Digite um valor para [{linha}, {item}]: ')))
print('-='* 45)
for x in range(0, 3):
    for c in range(0, 3):
        print('[ {} ]'.format(matriz[x][c]), end='')
    print()