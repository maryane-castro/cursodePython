#Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.
# No final, mostre os 10 primeiros termos dessa progressão. 
prim = int(input('Qual o primeiro termo da P.A.?  '))
raz = int(input('Qual a razão da P.A.?  '))
limite = prim + raz*10
for pa in range(prim, limite, raz):
    print(pa, end = '  ->  ')
print('ACABOU')