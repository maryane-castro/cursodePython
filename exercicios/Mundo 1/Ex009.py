#Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada
n = int(input('Digite um numero:  '))
red = '\033[1;31m'
gre = '\033[1;32m'
yel = '\033[1;33m'
blu = '\033[1;34m'
mag = '\033[1;35m'
cya = '\033[1;36m'

print(red, n, 'X 1 =', n)
print(gre, n, 'X 2 =', n * 2)
print(yel, n, 'X 3 =', n * 3)
print(blu, n, 'X 4 =', n * 4)
print(mag, n, 'X 5 =', n * 5)
print(cya, n, 'X 6 =', n * 6)
print(red, n, 'X 7 =', n * 7)
print(gre, n, 'X 8 =', n * 8)
print(yel, n, 'X 9 =', n * 9)
print(blu, n, 'X 10 =', n * 10)