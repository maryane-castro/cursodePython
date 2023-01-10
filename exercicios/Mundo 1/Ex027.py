#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nome = str(input('Digite um nome completo:  '))
splited = nome.split()
print('Primeiro nome:', splited[0])
print('Ultimo nome:', splited[-1])
