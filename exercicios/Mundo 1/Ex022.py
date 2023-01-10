#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo?  '))
lista = nome.split()
print("""
Seu nome com todas as letras maiusculas seria: {} 
Seu nome com todas as letras minusculas seria: {}
Seu nome completo possui {} letras.
Seu primeiro nome possui {} letras.
""".format(nome.upper(), nome.lower(), len(''.join(lista)), len(lista[0])))
