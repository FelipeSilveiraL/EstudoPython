print('Quer comprar uma casa?. Então vamos te oferecer um emprestimo!')
print('-=-' * 20)
print('mais antes vamos ver se \033[32m aprova!\033[m')
print('-=-' * 20)

salario = float(input('Qual é o valor do seu salário: R$ '))
casa = float(input('Qual é o valor da casa: R$ '))
parcelas = float(input('Quantas anos você irá pagar? '))
porcentagem = 30

"""PEGANDO O TOTAL DE PARCELAS"""
numParcelas = parcelas * 12

"""PEGANDO O VALOR DE CADA PARCELA"""
valorPagar = casa / numParcelas

"""PARA SABER O VALOR DE 30% DO SALÁRIO"""
valorLimiteSalario = (salario * porcentagem) / 100

""""VALIDANDE SE FOI APROVADO OU NÃO O IMPRESSTIMO"""
if (valorPagar > valorLimiteSalario):
    print('\033[31mDesculpe o valor da parcela será R${:.2f}, e isso é maior que {}% do seu salário que é R${:.0f}. Então não foi aprovado\033[m'.format(valorPagar, porcentagem, salario))
else:
    print('\033[32mOba o seu imprestimo para a compra da sua casa foi aprovado! Parabéns\033[m')