#Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso crie duas listas extras que vão conter apenas os valores pares e os impares digitados, respectivamente.
#  No final, mostre o conteudo das tres listas geradas.
cont = ''
lis = []
par = []
impar = []
while cont != 'N':
    num = int(input('Digite um numero:  '))
    lis.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
    while True:
        cont = str(input('Quer continuar?  ')).upper().strip()[0]
        if cont not in 'SN':
            print('Erro! Valor invalido, tente novamente.')
        else:
            break
print(f'Você digitou os numeros: {lis}')
print(f'Os numeros pares digitados são: {par}')
print(f'Os numeros impares digitados são: {impar}')