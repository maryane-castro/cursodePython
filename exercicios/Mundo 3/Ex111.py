'''Crie um pacote chamado utilidadesCeV que tenha dois modulos moeda e dado.
Transfira todas as funçoes utilizadas nos desafios 107, 109 e 109 para 
o primeiro pacote e mantenha tudo funcionando'''

from ex111m.utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)