dias = int(input('Por quantos dias o carro foi alugado?  '))
km = float(input('Quantos quilometros foram percorridos com o carro?  '))
preço = (dias * 60) + (km * 0.15)
print('O preço pelo aluguel do carro será R${:.2f}'.format(preço))