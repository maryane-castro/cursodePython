#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
adj = float(input('Qual o comprimento do cateto adjacente?  '))
opo = float(input('Qual o comprimento do catelo oposto?  '))
print(math.sqrt(math.pow(adj,2) + math.pow(opo,2)))