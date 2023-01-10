#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Qual o preço original do produto?  '))
desc = p * 0.95
print('O produto custando R${:.2f}, passará a custar R${:.2f} com 5 por cento de desconto.'.format(p, desc))