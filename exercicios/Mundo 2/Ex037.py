#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de coversao:
# 1 para binario 
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um numero: '))
escolha = int(input('''Escolha uma das opçoes de conversão:
 [ 1 ] Conversor para Binario 
 [ 2 ] Conversor para OCTAL
 [ 3 ] Conversor para Hexadecimal
 Sua opção:  '''))
if escolha > 3 or escolha < 1:
    print('ERRO. Digite uma das escolhas.')
elif escolha == 1:
    num_bi = bin(num)
    print('O numero {} em binario é {}.'.format(num, num_bi[2:]))
elif escolha == 2:
    num_oc = oct(num)
    print('O numero {} em Octal é {}.'.format(num, num_oc[2:]))
else:
    num_hexa = hex(num)
    print('O numero {} em Hexadecimal é {}.'.format(num, num_hexa[2:]))