'''Adapte o codigo do desafio 107, criando uma função chamada moeda() 
que consiga mostrar os valores como um valor monetário formatado.'''

from ex108m import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')