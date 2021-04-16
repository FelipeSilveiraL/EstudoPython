salario = float(input('Insira o salario do funcionario para saber qual será o seu aumento: '))

quinze = 15

dez = 10

if (salario <= 1250):
    calculo = 1250 * quinze / 100
    print('Tera um aumento de {}%, sendo assim o salario ficará de R${}'.format(quinze, (calculo + salario)))
else:
    calculo = 1250 * dez / 100
    print('Tera um aumento de {}%, sendo assim o salario ficará de R${}'.format(dez, (calculo + salario)))