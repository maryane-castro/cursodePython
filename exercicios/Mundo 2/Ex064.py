#Crie um program que leia varios numeros inteiros pelo teclado.
#O program só vai parar quando o usuario digitar o valor 999.
#que é a condição de parada. No final, mostre quantos numeros foram digitados 
# e qual foi a soma entre eles. 
n = 0
soma = 0
c = 0
print('Digite uma serie de numeros, 999 é a chave para parar,')
while n != 999:
    n = int(input('Digite um numero:  '))
    if n != 999:
        soma += n
        c += 1
print('Voce digitou {} numeros, a soma entre eles é {}.'.format(c , soma))
