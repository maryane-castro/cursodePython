#Crie um programa que leia o nome e o preço de varios produtos.
# O programa deverá perguntar se o usuario vai continuar. No final, mostre:
# X A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de 1000 reais.
# C) Qual é o nome do prodito mais barato.
s = mil = barat = nome_barat = 0
while True:
    cont = ''
    pro = input('Digite um produto:  ')
    preço = float(input('O produto custa R$'))
    s += preço
    if preço > 1000:
        mil += 1
    if barat == 0 or preço < barat:
        barat = preço
        nome_barat = pro
    while cont != 'S' and cont != 'N':
        cont = input('Quer continuar?[S/N]  ').upper()
    if cont == 'N':
        print('-'*20)
        print('Acabou, volte sempre')
        break
print('-'*15 + 'Fim do Programa' + '-'*15)
print(f'O total da compraa foi R${s:.2f}')
print(f'Temos {mil} produtos custam mais de R$1000.00.')
print(f'O produto mais barato é o {nome_barat} que custou R${barat:.2f}')
    