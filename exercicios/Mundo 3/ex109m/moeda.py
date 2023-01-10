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