#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha. 
spares = scoluna = 0
matriz = [[],[],[]] 
for linha in range(0,3):
    for item in range(0,3):
        matriz[linha].insert(item, int(input(f'Digite um valor para [{linha}, {item}]: ')))
        if matriz[linha][item] % 2 == 0:
            spares += matriz[linha][item]
        if item == 2:
            scoluna += matriz[linha][2]
print('-='* 45)
print(f'SOMA DOS PARES {spares}')
print(f'SOMA DOS ITENS DA 3° COLUNA {scoluna}')
print(f'O MAIOR ITEM DA SEGUNDA LINHA É O {max(matriz[1])}')
for x in range(0, 3):
    for c in range(0, 3):
        print('[ {} ]'.format(matriz[x][c]), end='')
    print()