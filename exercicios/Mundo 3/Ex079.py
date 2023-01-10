# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero já exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores digitados, em ordem crescente.
cont = ''
lis = []
while cont != 'N':
    num = int(input('Digite um numero:  '))
    if num not in lis:
        print('Valor adicionado com sucesso...')
        lis.append(num)
    else:
        print('Valor duplicado! Não vou adicionar.')
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continuar?[S/N]  ')).upper().strip()
        if cont != 'S' and cont != 'N':
            print(f'"{cont}" não é uma esposta valida, tente novamente!')
    if cont == 'N':
        print('Parando contagem...')
        break
    cont = ''
print('-=' * 35)
print(f'Foram digitados os numeros: {sorted(lis)}')
    