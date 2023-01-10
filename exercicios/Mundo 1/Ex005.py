#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um numero:  '))

print('O antecessor do seu numero é \033[4;34m{}\033[m,\nE o sucessor é \033[4;31m{}\033[m.'.format((num-1), (num+1)))