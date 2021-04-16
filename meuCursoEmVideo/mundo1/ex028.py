from random import randrange

numUsuario = int(input('Estou pensando em um numero de 0 a 5, qual é esse numero?: '))

numComputador = randrange(0, 5)

if (numUsuario == numComputador):
    print('Parabens!!! \n o numero que eu estava pensando era {}'.format(numComputador))
else:
    print('Ops!! não foi dessa vez \n o numero que eu estava pensando era {}'.format(numComputador))