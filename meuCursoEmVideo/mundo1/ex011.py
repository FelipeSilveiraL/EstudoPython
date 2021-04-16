print('Quer saber quantos litros de tinta vai para pintar a sua parede?\n então fornaça os dados abaixo em metros!')

l = float(input('Largura : '))
a = float(input('Altura : '))

area = l * a

tinta = 2

print('sua area deu {}m², então você irá precisade de {} litros de tinta!'.format(area, (area / tinta)))

