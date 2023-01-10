# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10 % de desconto
# a vista no cartao: 5% de desconto
# em até 2X no cartao: preço normal
# 3X ou mais no cartao; 20% de juros 
preço = float(input('O preço do produto:  '))
print('CONDIÇÕES DE PAGAMENTO: \n [ 1 ] À vista dinheiro/cheque: 10 % de desconto\n [ 2 ] À vista no cartão: 5% de desconto.\n [ 3 ] Em até 2X no cartão: Preço normal\n [ 4 ] 3X ou mais no cartão: 20% de juros.')
forma = int(input('A forma de pagamento:  '))
if forma == 1:
    print('O produto de preço R${:.2f} irá custar R${:.2f} com 10% de  desconto.'.format(preço, preço * 0.9))
elif forma == 2:
    print('O produto de preço R${:.2f} irá custar R${:.2f} com 5% de desconto.'.format(preço, preço * 0.95))
elif forma == 3:
    print('O produto custará R${:.2f}, o preço não foi alterado.'.format(preço))
elif forma == 4:
    print('O produto de preço R${:.2f}, irá custar R${:.2f} com os 20% de Juros.'.format(preço, preço * 1.2))
else:
    print('ERRO! Digite uma das 4 alternativas pelo numero.')