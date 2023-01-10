#Crie um programa que tenha uma tupla com varias palavras(não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quias são as suas vogas.
tupla = ('banana', 'arvore', 'cidade', 'floresta', 'passaro', 'flores', 'ooooo' , 'uuuu' , 'pppp')
for c in tupla:
    print('Na palavra {0}, temos: {1}{2}{3}{4}{5}'.format(c.upper(), 'a ' * c.count('a'), 'e ' * c.count('e'), 'i ' * c.count('i'), 'o ' * c.count('o'), 'u ' * c.count('u')))
    
    '''TENTATIVAS
    aa = ee = ii = oo = uu = 
    if 'a' in c:
        aa = True
    if 'e' in c:
        ee = True
    if 'i' in c:
        ii = True
    if 'o' in c:
        oo = True
    if 'u' in c:
        uu = True
    

for num, letra in enumerate(c):
    if letra in 'aeiou':
        print(c)'''