velocidadeCarro = int(input('Qual é a sua velocidade? '))

velocidadeMaxima = 100

multa = 7

if (velocidadeCarro <= velocidadeMaxima):
    print('ótima velocidade, não passse mais de {}km/h -- Boa Viajem!!'.format(velocidadeMaxima))
else:
    calculoMulta = (velocidadeCarro - velocidadeMaxima) * 7

    print('Multado! você exedeu o limite maximo que é de {}km/h \n Você deve pagar uma multa de R${}.00! \n Tenha um bom dia! diriga com segurança'.format(velocidadeMaxima, calculoMulta))