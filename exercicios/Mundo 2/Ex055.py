#Faca um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos 
lista = []
for c in range(0,5):
    lista.append(float(input('Qual o peso da pessoa numero {}?'.format(c + 1))))
sort = sorted(lista)
print('A pessoa mais pesada possui {}Kgs.'.format(sort[4]))
print('A pessoa mais leve possui {}Kgs.'.format(sort[0]))
