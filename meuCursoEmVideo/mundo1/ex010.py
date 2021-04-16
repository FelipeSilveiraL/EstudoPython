money = float(input('Quer comprar em dolar ?\n então me diga quanto você tem em reais: R$'))

dolarHoje = 0.19 #Dolar com a cotação do dia 02/12/2020

convertendo = money * dolarHoje

print('Com R$ {} você pode comprar $ {:.2f} Dolares'.format(money, convertendo))