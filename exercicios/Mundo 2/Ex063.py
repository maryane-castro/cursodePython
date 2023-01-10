#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Limite da sequencia de fibonacci:  '))-1
n1 = 1
n2 = 0
c = 0
print('0 ->', end=' ')
while c < n:
    n1 += n2
    n2 += n1
    print(n1, '->', end=' ')
    c += 1
    if c < n:
        print(n2, '->',end=' ')
    c += 1
print('FIM!')