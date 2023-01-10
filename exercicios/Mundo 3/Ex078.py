#Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lis = [int(input(f'Digite um numeropara a posição {x}:  ')) for x in range(0, 5)]
maior = max(lis)
menor = min(lis)
print(f'Você digitou os valores: ', *lis,sep=', ')
print(f'O maior numero é o {maior} e está na(s) posição(ões): ', end='')
for ind, item in enumerate(lis):
    if item == maior:
        print(f'{ind}...', end='')
print(f'\nO menor numero é o {menor} e está na(s) posição(ões): ', end='')
for ind2, item2 in enumerate(lis):
    if item2 == menor:
        print(f'{ind2}...', end='')
