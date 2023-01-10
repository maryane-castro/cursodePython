#crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade(21) e quantas jaa são maiores.
from datetime import date
ano = date.today().year
maior = 0
lista = []
for c in range(0 , 7):
    lista.append(ano - int(input('Digite o ano de nascimento:  ')))
    if lista[c] >= 21:
        maior += 1
print('Entre as datas de nascimento, {} das pessoas são maiores de idade, e {} são menores.'.format(maior, 7 - maior))
