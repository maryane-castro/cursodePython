# faça um programa que calcule a soma entre todos os numeros impares que 
# são multiplos de 3 e que se encontrem no intervalo de 1 até 500
soma = 0
for num in range(1, 501):
    if num % 2 == 1 and num % 3 == 0:
        soma += num
print(soma)