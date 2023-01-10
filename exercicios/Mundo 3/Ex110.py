'''Adicione ao modulo moeda.py criado nos desafios anteriores, uma função 
chamada resumo(), que mostre na tela algumas informações geradas pelas funções 
que ja temos no modulo criado até aqui.'''

from ex110m import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)#         moeda.resumo(Valor, % de Aumento, % de Diminuição)