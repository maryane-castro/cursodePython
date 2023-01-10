# Crie um programa que leia nome e duas notas de varios alunos e quarde tudo em uma lista composta.
# No final. mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
alunos = []
info = []
cont = ''
while cont != 'N':
    nome = str(input('Nome:  ')).title()
    notas = [float(input(f'Nota {n}:  ')) for n in range(1,3)]
    info.extend([nome, notas[:]])
    alunos.append(info[:])
    info.clear()
    while True:
        cont = str(input('Quer continuar?[S/N]  ')).strip().upper()[0]
        if cont not in 'SN':
            print('Erro! Resposta invalida, Tente novamente.')
        else: 
            break
print('-='* 25)
print('No.  NOME             MÉDIA')
print('-'* 50)
for num, aluno in enumerate(alunos):
    print('{:<5}{:<17}{}'.format(num, aluno[0], sum(aluno[1])/2))
print('-'* 50)
qlalu = ''
while qlalu != 999:
    while True:
        qlalu = int(input('Mostrar nota de qual aluno? (999 interrompe):  '))
        if qlalu == 999:
            break
        elif qlalu > len(alunos)-1:
            print('Erro! Aluno inexistente.')
        else:
            break
    if qlalu == 999:
        break
    else:
        print(f'Notas de {alunos[qlalu][0]} são: {alunos[qlalu][1]}')
        print('-'* 50)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')