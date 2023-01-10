#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-lo por extenso
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = ''
while True:
    num = int(input('Digite um numero de 0 a 20:  '))
    if num < 0 or num > 20:
        print('Tente novamente. ', end = '')
    else:
        print(f'Voce digitou o numero {extenso[num]}.')
        break
