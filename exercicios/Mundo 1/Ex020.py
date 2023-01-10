#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a1 = input('Primeiro aluno:  ')
a2 = input('Segundo aluno:  ')
a3 = input('Terceiro aluno:  ')
a4 = input('Quarto aluno:  ')
alu = [a1, a2, a3, a4]
shuffle(alu)
print('='*20, '\n1- {}\n2- {}\n3- {}\n4- {}\n'.format(alu[0], alu[1], alu[2], alu[3]) + '='*20)

'''
print('1-',alu[0])
print('2-',alu[1])
print('3-',alu[2])
print('4-',alu[3])'''