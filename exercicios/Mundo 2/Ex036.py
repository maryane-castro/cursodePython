# Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo será negado. 
valor = int(input('Digite o valor da casa:  '))
salario = int(input('Qual seu salario?  '))
anos = float(input('Em quantos anos você deseja pagar o emprestimo da casa?  '))
mensal = valor / (anos * 12) #valor mensal da prestação
print('\033[1;33mPara pagar uma casa de R${:.2f} em {:.0f} ano(s), a prestação será R${:.2f} por mês.\033[m'.format(valor, anos, mensal))
if mensal < salario*0.3: #aqui verifica se o valor mensal é menor que 30% do salario
    print('\033[1;32mACESSO CONCEDIDO!\033[m')
else: 
    print('\033[4;31mACESSO NEGADO, lamentamos, mas seu salario não é suficiente.\033[m')

