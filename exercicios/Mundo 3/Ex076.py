#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular 
tupla = ('Caderno', 13.5 , 'Borracha', 0.99 , 'Lapis' , 1.50 , 'Banana', 3.75 , 'Estojo', 35, 'Transferidor', 4.20 , 'Compasso' , 9.99 , 'Mochila' , 120.32)
print('{0}\n{1:^40}\n{0}'.format('=' * 40, 'LISTAGEM DE PREÇOS'))
for ind, item in enumerate(tupla):
    if ind % 2 == 0:
        print(f'{item:.<30}', end = '')
    else: 
        print(f'R${item:>7.2f}')
print('-' * 40)