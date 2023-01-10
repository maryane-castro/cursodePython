'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
á função input() do python, só que fazendo a validação para aceitar apenas um valor numerico.
Ex.: n = leiaInt("Digite um numero:  ")'''

def leiaInt(string):
    num = ''
    while num.isnumeric() == False:
        num = input(string)
        if num.isnumeric() == False:
            print('\033[31mErro! Digite um numero inteiro válido.\033[m')
    return num

print(leiaInt('Digite algo:  '))