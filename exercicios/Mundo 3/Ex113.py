'''Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um numero de tipo inválido.
Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(perg):
    while True:
        try:
            num = input(perg)
            int(num)
        except ValueError:
            print('ERRO! Numero Inteiro inválido.')
        except KeyboardInterrupt:
            print('\nUsuario preferiu não digitar esse numero')
            return 0
        else:
            return num
def leiaFloat(perg):
    while True:
        try:
            num = input(perg)
            float(num)
        except ValueError:
            print('Erro! Numero Real inválido!')
        except KeyboardInterrupt:
            print('\nUsuario preferiu não digitar esse numero')
            return 0
        else:
            return num


inteiro = leiaInt('Digite um número Inteiro:  ')
quebrado = leiaFloat('Digite um número Real:  ')
print(f'O valor inteiro foi {inteiro} e o valor real foi {quebrado}.')