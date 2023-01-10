#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o 
soma = 0
for vzs in range(0, 6):
    num = int(input('Digite um numero:  '))
    if num % 2 == 0:
        soma += num
print(soma)