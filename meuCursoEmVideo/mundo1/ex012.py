produto = float(input('Qual é o valor do Produto R$'))

desconto = float(input('Valor do desconto: '))

diminuir = (produto *  5) / 100

valor = produto - diminuir

print('O valor com o desconto de {:.1f}% será R$ {}, descontando assim R$ {}'.format(desconto, valor, diminuir))