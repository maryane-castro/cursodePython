'''dados = open('Exercicios/Mundo 3/Ex115DataBase.txt', 'a+')
lst = []
for x in lst:
    dados.write(x)
    dados.write('\n')
dados.seek(0)
print(dados.read())'''
dados = open('Exercicios/Mundo 3/Ex115DataBase.txt', 'a+')

def linha(frase, lfinal = True):
    print('~'* 40)
    print('{}{}'.format(" "* (20 - len(frase)//2),frase))
    if lfinal:
        print('~'* 40)

def escolha(perg):
    while True:
        try:
            resp = int(input(perg))
        except:
            print('Erro! Tente novamente.')
        else:
            if resp >= 1 and resp <= 3:
                return resp
            else:
                print('ERRO! Digite uma opção válida entre 1 e 3.')
def PCadas():
    linha('PESSOAS CADASTRADAS')
    dados.seek(0)
    print(dados.read())

def CadasN(nome, idade):
    dados.write(f'{nome.title():30}{idade} anos\n')
    print(f'Novo registro de {nome} adicionado')