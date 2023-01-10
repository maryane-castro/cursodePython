#faça um programa que leia a largura e altura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necssaria para pintá-la, 
#sabendo que cada litro de tinta pinta uma area de 2m²
larg = float(input('Qual a largura da parede em metros?  '))
alt = float(input('Qual a altura da parede em metros?  '))
area = larg * alt
tinta = area / 2
print('A parede possui area de {}m², e precisaria de {} litros de tinta para pintar uma demão.'.format(area, tinta))