print('Analisando triangulo')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('Os seguementos acima PODEM FORMAR triângulo - ', end='')#END-nesse caso esta eliminando a quebra de linha

    if(r1 == r2 or r1 == r3 or r2 == r3):
        print('ele é um Isóceles')
    elif (r1 == r2 and r2 == r3 and r1 == r3):
        print('ele é um Equilátero')
    else:
        print('ele é um Escaleno') 

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')