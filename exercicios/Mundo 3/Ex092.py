#Crie um programa que leia nome, ano de cascimento e carteira de trabalho e cadastre-os (com idade) em um discionario, 
# Se por acaso a CTPS for diferente de ZERO, o discionario receberá tambem o ano de contratação e o salario.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar
from datetime import date
ano_atual = date.today().year
perfil = {}
perfil['nome'] = str(input('Nome:  '))
ano_nsc = int(input('Ano de nascimento:  '))
perfil['idade'] = ano_atual - ano_nsc
perfil['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
if perfil['ctps'] != 0:
    perfil['contratação'] = int(input('Ano de contratação:  '))
    perfil['salario'] = float(input('Salário:  '))
    perfil['aposentadoria'] = perfil['contratação'] - ano_nsc + 35
print('-='* 30)
print(perfil)
for x in perfil.items():
    print(f'{x[0]} tem valor {x[1]}')