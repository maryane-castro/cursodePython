'''Crie um pequeno sistema modularizado que permite cadastrar 
pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema so vai ter 2 opções: cadastrar uma nova pessoa e listar 
todas as pessoas cadastradas.'''

from ex115m import Uteis
from time import sleep as sl
import cores as c
dados = open('Exercicios/Mundo 3/Ex115DataBase.txt', 'a+')
limpar = c.cor[1]['sem']
azul = c.cor[1]['blue']
verde = c.cor[1]['green']


while True:
    Uteis.linha('MENU PRINCIPAL', False)
    Uteis.linha(
'''1- {0}Ver pessoas cadastradas.{1}
2- {0}Cadastrar nova pessoa.{1}
3- {0}Sair do Sistema.{1}'''.format(azul, limpar))
    esco = Uteis.escolha('{}Sua opção >>{}'.format(verde, limpar))
    if esco == 1:
        Uteis.PCadas()
        sl(1.0)
    if esco == 2:
        Uteis.linha('NOVO CADASTRO')
        nome = input('Qual o nome?  ')
        idade = input('Qual a idade?  ')
        Uteis.CadasN(nome, idade)
        sl(1)
    if esco == 3:
        Uteis.linha('SAINDO DO SISTEMA... ATÉ LOGO!')
        break
    