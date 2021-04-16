import math

oposto = float(input('Insira um valor para o Cateto Oposto: '))

adjacente = float(input('Insira um valor para o Cateto Adjacente: '))

print('A Hipotenusa vai medir {:.2f}'.format(math.hypot(oposto, adjacente)))