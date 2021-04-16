print('calculando o IMC')
print('-' * 20)

#dados sendo informado pelo usuário

peso = float(input('Informe seu peso(kg): '))
altura = float(input('Informe sua altura(Metro): '))


#realizando o calculo
imc = peso / (altura ** 2)# altura ao quadrado


#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#ACima dos 40: Obesidade mórbida

#mostrando pro usuário
if (imc < 18.5):
    print('Seu IMC é {:.1f}, então você está ABAIXO DO PESO, cuidado!'.format(imc))
elif(imc >= 18.5 and imc <= 25):
    print('Seu IMC é {:.1f}, então você está PESO IDEAL!'.format(imc))
elif(imc > 25 and imc <= 30):
    print('Seu IMC é {:.1f}, então você está SOBREPESO!'.format(imc))
elif(imc > 30 and imc <= 40):
    print('Seu IMC é {:.1f}, então você está OBESIDADE!'.format(imc))
else:
    print('Seu IMC é {:.1f}, então você está OBESIDADE MORBIDA, cuidado!'.format(imc))