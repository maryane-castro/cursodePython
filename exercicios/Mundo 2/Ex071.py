#Crie um programa que sinule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario
# qual será o valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada 
# valor serão entregues. Obs. Considere que o caixa possui cedulas de R$50, R$20,R$10 e R$1
print('=' * 30 + '\nBANCO CENTRAL DO BRASIL\n' + '=' * 30)
val = int(input('Digite o valor que quer sacar: R$'))
c = v = d = 0
if val >= 50:
    c = val // 50
    val -= 50 * c
if val >= 20:
    v = val // 20
    val -= 20 * v
if val >= 10:
    d = val // 10
    val -= 10 * d
print('=' * 30)
print(f'Total de {c} cedulas de R$50')
print(f'Total de {v} cedulas de R$20')
print(f'Total de {d} cedulas de R$10')
print(f'Total de {val} cedulas de R$1')