'''Faça um programa que tenha uma função chamada escreva(), que receba um 
texto qualquer como parametro e mostre uma mensagem com temanho adaptável'''
def escreva(txt):
    tama = len(txt) + 4
    print('~'* tama)
    print(f'  {txt}  ')
    print('~'* tama)


escreva('Curso Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')