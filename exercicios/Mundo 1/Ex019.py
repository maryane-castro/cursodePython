#Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolido
from random import choice
a1 = input('Primeiro aluno:  ')
a2 = input('Segundo aluno:  ')
a3 = input('Terceiro aluno:  ')
a4 = input('Quarto aluno:  ')
print('O aluno escolhido será: ', choice([a1, a2, a3, a4]))