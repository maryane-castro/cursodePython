# Crie um programa onde o usuario possa digitar cinco valores numericos 
# e cadastre-os em uma lista, ja na posição correta de insersão(sem usar o sort()).
# No final mostre a lista ordenada na tela.

lis = []
for c in range(0,10):
    num = int(input('Digite um numero:  '))
    if lis:
        if num >= max(lis):
           lis.append(num)
           print('Adicionado ao final da lista...')
        if num <= min(lis):
            lis.insert(0, num)
            print('Adicionado ao começo da lista...')
        elif num > min(lis) and num < max(lis):
            for item in lis:
                if num < item:
                    lis.insert(lis.index(item), num)
                    print(f'Adicionado na posição {lis.index(item)-1} da lista...')
                    break
    else:
        lis.append(num)
        print('Adicionado ao final da lista...')
    print(lis)