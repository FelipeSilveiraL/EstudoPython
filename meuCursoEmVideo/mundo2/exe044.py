"""
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros 
"""

#Coletando o valor da compra
valor = float(input('Informe o valor da compra: R$'))
print('-' * 30)

#Coletando a forma de pagamento
print('FORMA DE PAGAMENTO:')

pagamento = int(input(
                        '[1] à vista dinheiro/cheque\n'
                        '[2] à vista no cartão\n'
                        '[3] Parcelar no cartão\n'
                        'Qual a opção: '
                        ))
#caso a forma seja parcelamento, coletando quantas vezes no cartão
if(pagamento == 3):
    print('-' * 30)
    quantidadeParcelas = int(input('Quantas Vezes: '))


#realizando o calculo e informando o usuário

if(pagamento == 1):
    #calculando 10% de desconto

    desconto = (valor * 10) / 100
    valorPagar = valor - desconto

    print('Sua compra terá um desconto de 10%, então o valor de R${} irá passar a custar R${}'.format(valor, valorPagar))
elif(pagamento == 2):
    #calculando 5% de desconto
    desconto = (valor * 5) / 100
    valorPagar = valor - desconto

    print('Sua compra terá um desconto de 5%, então o valor de R${} irá passar a custar R${}'.format(valor, valorPagar))
else:

    if(quantidadeParcelas <= 2):

        valorParcela = valor / quantidadeParcelas

        print('Sua compra será parcelada em {}x, então o valor de cada parcela será R${}, totalizando R${} SEM JUROS'.format(quantidadeParcelas, valorParcela, valor))
    else:

        #calculando juros
        juros = (valor * 20) / 100
        valorJuros = valor + juros

        valorParcela = valorJuros / quantidadeParcelas

        print('Sua compra será parcelada em {}x, com juros de 20%, cada parcela será R${}, totalizando R${}'.format(quantidadeParcelas, valorParcela, valorJuros))