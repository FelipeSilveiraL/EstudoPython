num1 = float(input('Insira um numero: '))
num2 = float(input('Insira outro numero: '))
num3 = float(input('Insira mais um numero: '))

print('Vamos agora ver dos quais desses numeros e o maior e qual é o menor')
print('=-=' * 20);

menor = num1

if (num2 < num1 and num2 < num3):
    menor = num2

if (num3 < num1 and num3 < num2):
    menor = num3

maior = num1

if (num2 > num1 and num2 > num3):
    maior = num2

if (num3 > num1 and num3 > num2):
    maior = num3

print('O numero MAIOR é {}'.format(maior))

print('o numero MENOR é {}'.format(menor))