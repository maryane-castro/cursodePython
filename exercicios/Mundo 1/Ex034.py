#escreva um programa que pergunta o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a R$1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
sal = int(input('Qual o salario do funcionario?  '))
if sal > 1250:
    al = sal * 1.1
else:
    al = sal * 1.15 
print('O salario de R${:.2f} do funcionario com aumento ficará R${:.2f}.'.format(sal, al))