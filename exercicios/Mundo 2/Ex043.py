# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela acaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25; peso ideal
# 25 até 30: sobrepeso
# 30 até 40 Obesidade
# acima de 40: Obesidade morbida
peso = float(input('Digite seu peso:  '))
alt = float(input('Digite sua altura:  '))
imc = peso / (alt ** 2) 
if imc < 18.5:
    status = 'Abaixo do peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc <= 40:
    status = 'Obesidade'
elif imc > 40:
    status = 'Obesidade morbida'
print('De acordo com seu IMC de {:.2f}, você está em {}.'.format(imc, status))
    