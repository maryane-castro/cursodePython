#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,desconsiderando os espaços.
frase = str(input('Digite uma frase ou palavra pra saber se é um palindromo:  ')).lower()
semesp = frase.replace(' ','')
leng = len(semesp)
letras_erradas = 0
for c in range(1, leng + 1):
    if semesp[c-1] != semesp[leng - c]:
        letras_erradas += 1
if letras_erradas != 0:
    print('Não é um polindromo, {} letras não batem.'.format(letras_erradas))
else:
    print('É um Palindromo!! Lendo de trás pra frende é a mesma coisa que lendo normalmente!')
    