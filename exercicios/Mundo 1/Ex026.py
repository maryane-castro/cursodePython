#faça m programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez  
frase = str(input('Escreva uma frase:  ')).lower()
print('A primeira letra A apareceu na posição {}.'.format(frase.find('a') + 1))
print('A letra A apareceu {} vezes na frase.'.format(frase.count('a')))
print('A letra A apareceu por ultimo na posição {}.'.format(frase.rfind('a') + 1))

