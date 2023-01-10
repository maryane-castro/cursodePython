#desenvolva um programa que leia as notas de um aluno, calcule e mostre sua media
nota1 = int(input('Digite a primeira nota:  '))
nota2 = int(input('Digite a segunda nota:  '))
media = (nota1 + nota2) / 2
if media >= 6:
    cor = '\033[1;32m'
else:
    cor = '\033[1;31m'
print('A media entre {} e {} é {}{}\033[m.'.format(nota1, nota2, cor, media))