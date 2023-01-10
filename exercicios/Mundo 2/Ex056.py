#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# A media de idade do grupo
# Qual é o homem mais velho
# quantas mulheres tem menos de 20 anos
nome = []
idade = []
sexo = []
homens = []
media = 0
qtas = 0
for c in range(0, 4, 1):
    print('======== {}° PESSOA ========'.format(c+1))
    nome.append(input('1- Nome:  '))
    idade.append(int(input('2- Idade:  ')))
    sexo.append(input('3- Sexo[M/F]:  ').upper())
    if sexo[c] == 'M':
        homens.append(idade[c])
    elif sexo[c] == 'F' and idade[c] < 20:
        qtas += 1
    media += idade[c] / 4
a = sorted(homens, reverse=True)
b = a[0]
print('A idade media é {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(b, nome[idade.index(b)]))
print('{} mulheres são mais jovens que 20 anos.'.format(qtas))






'''
#    nome = input('Digite o nome da pessoa: ')
    ida = idade.append(int(input('Digite a idade da pessoa:')))
#    sexo = input('Qual o sexo da pessoa:  ')'''