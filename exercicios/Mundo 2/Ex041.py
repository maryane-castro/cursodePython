# a confederação Nacional de natação precisa de um programa q leia o ano ne nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Ate 14 anos: INFANTIL
# Ate 19 anos: JUNIOR
# Ate 20 anos : SENIOR
# ACIMA: MASTER
from datetime import date
presente = date.today().year 
nasc = int(input('Digite o ano de nascença do aluno:  '))
idade = presente - nasc
if idade <= 9:
    modalidade = 'MIRIM'
elif idade <= 14:
    modalidade = 'INFANTIL'
elif idade <= 19:
    modalidade = 'JUNIOR'
elif idade <= 20:
    modalidade = 'SENIOR'
else:
    modalidade = 'MASTER'
    
print('O aluno nascido em {}, com {} anos, pertencerá a modalidade {}.'.format(nasc, idade, modalidade))
