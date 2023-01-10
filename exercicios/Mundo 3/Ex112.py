'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''

from ex112m.utilidadesCeV import moeda
from ex112m.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite um valor: R$')
moeda.resumo(p, 35, 22)