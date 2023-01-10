#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto. 
a = 0
while a < 1:
    genero = input('Digite o sexo de uma pessoa:  ').upper()
    if genero in 'FM':
        if genero == 'F':
            print('A pessoa é uma mulher.')
        else:
            print('A pessoa é um homem.')
        a += 1
    else:
        print('\033[1;31mErro! Digite um genero válido.\033[m')

    