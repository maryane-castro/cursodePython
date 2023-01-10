#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metro = int(input('Digite uma distancia em metros:  '))
centi = metro * 100
mili = metro * 1000
print(metro,'metros em centimetros é: \033[1;32m{}cm\033[m.\nEssa distancia em milimetros é: \033[1;34m{}mm\033[m.'.format(centi, mili))