#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite o nome de uma pessoa:  '))
print('O nome inserido possui "Silva"?', 'Silva' in nome.title())