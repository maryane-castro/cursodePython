from math import radians ,sin ,cos ,tan
angulo = float(input('Digite o angulo que você deseja:  '))
rad = radians(angulo)
print('O angulo de {} graus tem o seno de {:.2f}.'.format(angulo, sin(rad)))
print('O angulo de {} graus tem o coseno de {:.2f}.'.format(angulo, cos(rad)))
print('O angulo de {} graus tem a tangente de {:.2f}.'.format(angulo, tan(rad)))