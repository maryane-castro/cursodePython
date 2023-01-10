#Faça um programa que leia nome e média de um aluno, quardando tambem a situação em um dicionario.
# No final, mostre o conteudo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Qual o nome do aluno?  '))
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]}?  '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situaçao'] = 'Reprovado'
print(f'O nome é igual a {aluno["nome"]}.')
print(f'Média é igual a {aluno["media"]}.')
print(f'Situação é igual a {aluno["situaçao"]}')
