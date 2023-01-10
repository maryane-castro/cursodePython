#faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todas as informacoes possiveis sobre ela.
abc = input('Digite algo:   ')
cores = {'l' : '\033[m', 
'az' : '\033[1;34m',
'am' : '\033[1;33m',
'vem' : '\033[1;31m',
'ver' : '\033[1;32m'}
print(cores['az'], 'Otipo primitivo é', type(abc))
print(cores['am'], 'É alfanumerico?', abc.isalnum())
print(cores['vem'], 'É alfabetico?', abc.isalpha())
print(cores['ver'], 'É ascii?', abc.isascii())
print(cores['az'], 'É decimal?', abc.isdecimal())
print(cores['am'], 'É digito?', abc.isdigit())
print(cores['vem'], 'É identificador?', abc.isidentifier())
print(cores['ver'], 'É minusculo?', abc.islower())
print(cores['az'], 'É numerico?', abc.isnumeric())
print(cores['am'], 'É imprimivel?', abc.isprintable())
print(cores['vem'], 'Só tem espaços?', abc.isspace())
print(cores['ver'], 'É titulo?', abc.istitle())
print(cores['az'], 'É maiusculo?', abc.isupper(), cores['l'])