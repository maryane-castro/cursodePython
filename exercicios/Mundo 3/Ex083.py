#Crie um programa onde o usuario digite uma expressão qualquer que use parenteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados em ordem correta.
c = 0
exp = str(input('Digite uma expressão:  '))
for dig in exp:
    if dig == '(':
        c += 1
    elif dig == ')':
        c -= 1
if c == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')