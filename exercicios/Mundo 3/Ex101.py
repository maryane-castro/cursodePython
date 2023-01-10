'''Crie um programa que tenha uma função chamada voto() que vai receber como parametro
 o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
 tem voto NEGADO, OPSIONAL ou OBRIGATORIO nas eleições.'''

from datetime import datetime

def voto(idade):
    if idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        return 'NÃO VOTA'
    else:
        return 'VOTO OPCIONAL'


ano_nasc = int(input('Que ano você nasceu?  '))
idade = datetime.today().year - ano_nasc
print(f'Com {idade} anos:  {voto(idade)}')