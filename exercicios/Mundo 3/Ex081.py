#Crie um programa quue vai ler varios numeros e colocar em uma lista. Depois disso mostre:
#A) Quantos numeros foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e esta ou não na lista.
cont = '0'
lis = []
while cont != 'N':
    cont = '0'
    lis.append(int(input('Digite um numero:  ')))
    while cont not in 'SN':
        cont = str(input('Quer continuar?[S/N]  ')).upper().strip()[0]
        if cont in 'SN':
            break
        else:
            print('Erro! Resposta invalida, tente novamente')
print(f'Foram digitados {len(lis)} números.')
print('A lista ordenada de forma decrescente seria:', sorted(lis, reverse=True))
if 5 in lis:
    print('O numero 5 está na lista')
else:
    print('O numero 5 NÃO está na lista')