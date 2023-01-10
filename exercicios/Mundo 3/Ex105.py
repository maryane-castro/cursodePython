'''Faça um programa que tenha uma função notas() que pode receber várias notas 
de alunos e vai retornar um dicionario com as seguintes informaçoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A médioa da turma
- A situação(opcional)
Adicione tambem as docstrings da função'''

def notas(*n, sit = False):
    '''
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação da nota.
    :return: dicionário com várias informações sobre a situação da turma.'''
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n) / len(n)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 5:
            dic['situação'] = 'RAZOAVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


resp = notas(3, 4.5, 7, 2, 5, 9.5, sit=True)
print(resp)