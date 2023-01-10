#Crie um programa que leia varios numeros inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
s = 0
c = 0
maior = 0
menor = 0
continuar = 'S'
while continuar != 'N' and continuar == 'S':
    num = int(input('Digite um numero:  '))
    s += num
    c += 1
    if c == 1:
        num = maior = menor
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Quer continuar?[S/N]  ')).upper()
print('A media dos numeros é {:.2f}.'.format(s / c))
print('O maior numero digitado é o {}, e o menor numero é o {}.'.format(maior, menor))
