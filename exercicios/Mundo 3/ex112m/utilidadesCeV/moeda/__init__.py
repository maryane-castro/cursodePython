def l(n):
    print('~'* n)

def metade(num, moe = False):
    res = num / 2
    if moe:
        return moeda(res)
    else:
        return res

def dobro(num, moe = False):
    res = num * 2
    if moe:
        return moeda(res)
    else:
        return res

def aumentar(num, pcen, moe = False):
    res = num * (1 + pcen/100)
    if moe:
        return moeda(res)
    else:
        return res

def diminuir(num, pcen, moe = False):
    res = num * (1 - pcen/100)
    if moe:
        return moeda(res)
    else:
        return res

def moeda(resu):
    return f'R${resu:.2f}'

def resumo(num=0, au=0, red=0):
    l(32)
    print(f'{"RESUMO DO VALOR":^32}')
    l(32)
    print('{:<22}{}'.format('Preço analizado:', moeda(num)))
    print('{:<22}{}'.format('Dobro do preço:', dobro(num, True)))
    print('{:<22}{}'.format('Metade do preço:', metade(num, True)))
    print('{:<22}{}'.format(f'{au}% de aumento:', aumentar(num, au, True)))
    print('{:<22}{}'.format(f'{red}% de redução:', diminuir(num, red, True)))
    l(32)