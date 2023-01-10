#Refaça o exercicio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for
num = int(input('Digite um numero para mostrar a tabuada:  '))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num*c))