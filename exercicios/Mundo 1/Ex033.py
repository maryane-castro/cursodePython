#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um numero:  '))
n2 = int(input('Digite mais um numero:  '))
n3 = int(input('Digite outro numero:  '))

#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior numero é o {}.'.format(maior))
print('O menor numero é o {}.'.format(menor))
'''tentativa 1 :
if n1 < n2 and n1 < n3:
    menor = n1
    if n2 > n3:
        maior = n2
    else:
        maior = n3
if n2 < n3 and n2 < n1:
    menor = n2
    if n1 > n3:
        maior = n1
    else:
        maior = n3
if n3 < n1 and n3 < n2:
    menor = n3
    if n1 > n2:
        maior = n1
    else:
        maior = n2'''
'''tentativa 2 :
if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
    else: #n1 esta no meio
        if n2 > n3:
            maior = n2
            menor = n3
        else:
            maior = n3
            menor = n2
else:
    if n1 < n3:
        menor = n1
        if n2 < n3:
            maior = n3
    else: #n1 esta no meio
        if n2 > n3:
            maior = n2
            menor = n3
        else:
            maior = n3
            menor = n2'''