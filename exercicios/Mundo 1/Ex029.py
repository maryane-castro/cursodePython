#Escreva um programa que leia a velocidade de um carro
#Se ela ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7.00 por cada km acima do limite
vel = int(input('Qual a velocidade do seu carro em Km/h? '))
if vel > 80:
    multa = (vel - 80)* 7
    print('Você passou da velocidade permitida de 80Km/h, passou a {}Km/h, e sua multa será R${:.2f}.'.format(vel, multa))
else:
    print('Você esta no limite de velocidade de 80Km/h,')