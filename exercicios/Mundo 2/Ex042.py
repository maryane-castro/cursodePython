# Refaça o desafio 035 dos triangulos, acrecentando o recurso de mostrar que tipo de triangulo será formado:
# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes.

r1 = float(input('Digite o comprimento da reta 1:  '))
r2 = float(input('Digite o comprimento da reta 2:  '))
r3 = float(input('Digite o comprimento da reta 3:  '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo')
    if r1 == r2 == r3:
        print('Irá format um triangulo EQUILÁTERO.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Irá formar um triangulo ISOSCELES.')
    elif r1 != r2 != r3:
        print('Irá format um triangulo ESCALENO.')
else:
    print('As retas NÃO podem formar um triangulo.')