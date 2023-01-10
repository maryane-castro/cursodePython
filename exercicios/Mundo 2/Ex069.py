#Crie eum programa que leia a idade e o sexo de verias pessoas.
#  A cada pessoa cadastrada o programa deverá perguntar se o usuario
#  quer ou não continuar. No final, mostre;
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos. 
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade:  '))
    sexo = ''
    while sexo not in 'FM':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ''
    while resp not in 'SN':
        resp = input('Quer continuar?  ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')


'''
c = maior = menor = hom = gen = 0
while True:
    c += 1
    continuar = gen = ''
    idade = int(input(f'Qual a idade da pessoa {c}?  '))
    if idade > 18:
        maior += 1
    while continuar != 'S' and continuar != 'N' or gen != 'F' and gen != 'M':
    
        gen = input(f'Qual o sexo da pessoa{c}?[F/M] ').upper()
        continuar = input('Quer continuar? [S/N]  ').upper()
        print('-'*20)
        if continuar not in 'SN' or gen not in 'FM':
            print('Erro! Tente Novamente.')
    if gen == 'M':
        hom += 1
    if gen == 'F' and idade < 20:
        menor += 1
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar? [S/N]  ').upper()
        if continuar not in 'SN':
            print('Erro! Tente Novamente.')
        
    if continuar == 'N':
        break

print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{hom} homens foram cadastrados.')
print(f'{menor} mulheres tem menos de 20 anos.')'''
    