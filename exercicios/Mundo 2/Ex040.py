#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
# Média abaixo de 5.0: REPROVADO
# Media entre 5.0 e 6.9: RECUPERAÇÃO
# Media 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do aluno:  ')) 
nota2 = float(input('Digite a segunda nota do aluno:  '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO')
elif media >= 7.0:
    print('APROVADO!')
else: #media entre 5 e 6.9:
    print('RECUPERAÇÃO')