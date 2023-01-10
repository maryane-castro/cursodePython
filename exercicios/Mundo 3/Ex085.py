# Crie um programa onde o usuario possa digitar 7 valores numericos, 
# e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
numeros = [[],[]]
for x in range(0,7):
    num = int(input(f'Digite o {x+1}° numero:  '))
    if num % 2 == 0:
        numeros[0].append(num)
    else: 
        numeros[1].append(num)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')