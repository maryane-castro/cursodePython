#Faça um programa que pergunte o nome de uma pessoa e faça uma menssagem de boas vindas
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}{}{}!'.format('\033[1;34m', nome, '\033[m'))