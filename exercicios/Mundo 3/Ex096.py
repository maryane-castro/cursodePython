'''Faça um programa que tenha uma função chamada area(), que receba as dimenções
de um terreno retangular(largura e comprimento) e mostre a área do terreno.'''
def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')
def pergunta(frase):
    return float(input(frase))


print(f'\n  Controle de terrenos \n{"-"*30}')
area(pergunta('Largura (m): '), pergunta('Comprimento (m):'))