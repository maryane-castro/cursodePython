#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario,com 15% de aumento
salar = float(input('Qual o salario do funcionario?  '))
novo = salar * 1.15
print('O novo salario do funcionario vai ser R${:.2f}'.format(novo)) 