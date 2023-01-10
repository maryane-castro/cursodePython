'''Crie um programa que tenha uma função fatorial() que receba dois parametros: 
o primeiro que indique o numero e calcular e o outro chamado show, que será um valor
logico(opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial.'''

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param num: O número a ser calculado, deve ser maior ou igual a 0.
    :param show: (opcional) mostra ou não a conta
    :return: O valor do fatorial de um numero"""
    f = 1
    lst = []
    for c in range(num,0,-1):
        f *= c
        lst.append(str(c))
    if num == 0:
        lst.append('0!')
    if show:
        return f"{' x '.join(lst)} = {f}"
    return f


print(fatorial.__doc__)
print(fatorial(5, True))
print(fatorial(0, True))
print(fatorial(2))
print(fatorial(9, True))
print(fatorial(1))