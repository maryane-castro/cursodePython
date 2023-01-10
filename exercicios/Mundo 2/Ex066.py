#Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999.
# que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles. 
n = s = c = 0
while True:
    n = int(input('Digite um numero (999 para parar):  '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Voce digitou {c} numeros, e a soma entre eles é {s}')
