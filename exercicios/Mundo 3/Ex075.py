#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares 
tup = (
int(input('Digite um numero: '))
, int(input('Digite um numero: '))
, int(input('Digite um numero: '))
, int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {tup.count(9)} vezes na tupla')
if 3 in tup:
    print(f'O primeiro valor 3 apareceu na posição {tup.index(3) + 1}°.')
else:
    print('Não apareceu nenhum 3 na tupla.')
print('Os numeros pares digitados são: ', end='')
for c in tup:
    if c % 2 == 0:
        print(c, end= ' ')
#listtostring = ' , '.join([str(elem) for elem in lista])  #Metodo de transformar lista em string