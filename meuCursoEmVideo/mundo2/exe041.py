from datetime import date

anoAtual = date.today().year

#Idade informada pelo usuário
anoNadador = int(input('Informe o ano de nascimento do nadador: '))

#Calculando data para saber a idade
idade = anoAtual - anoNadador

#Gerando a saida do programa

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÉNIOR
# Acima é MASTER

if(idade <= 9):
    print('Sua idade é {}, então você é MIRIM'.format(idade))
elif(idade <= 14):
    print('Sua idade é {}, então você é INFANTIL'.format(idade))
elif(idade <= 19):
    print('Sua idade é {}, então você é JUNIOR'.format(idade))
elif(idade <= 25):
    print('Sua idade é {}, então você é SÉNIOR'.format(idade))
else:
    print('Sua idade é {}, então você é MASTER'.format(idade))