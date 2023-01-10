#Faça um programa que leia um numero qualquer e mostre seu fatorial.
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
num = int(input('Digite um numero qualquer:  '))
prod = num
print(str(num)+'! =', end=' ')# 5! = ...
while num > 1:
    print(num, 'X', end=' ') #5 X 4 X 3 X 2 X ...
    prod = prod * (num - 1)
    num -= 1
print('1 =', prod)#... 1 = 120

    