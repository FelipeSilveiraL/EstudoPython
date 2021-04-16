km = float(input('Quantos R$ será a sua viagem, informe os KM/h para saber!: '))

poucokm = km * 0.50

muitoskm = km * 0.45

if(km >= 200):
    print('O custo da sua viagem será R${}'.format(muitoskm))
else:
    print('O custo da sua viagem será R${}'.format(poucokm))