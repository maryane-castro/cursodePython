#Crie um algoritmo que leia leia um numero e mostre o seu dobro, triplo, e raiz quadrada.
n = int(input('\033[1;33mDigite um numero:  '))
#dob = n * 2
#tri = n * 3
#rai = n ** (1/2)
print('Informações do numero digitado:\nO dobro: \033[4;34m{}\033[m\033[1;33m.\nO triplo: \033[1;32m{}\033[1;33m.\nA raiz quadrada: \033[1;31m{}\033[1;33m.\033[m'.format((n*2), (n*3), (n**0.5) ) )