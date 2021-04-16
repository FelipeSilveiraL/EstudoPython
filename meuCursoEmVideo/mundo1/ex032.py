from datetime import date

ano = int(input('Quer saber se o ano é bisexto?, insira um Ano '))

#caso o usuário não preencha o ano então irá mostrar o ano atual
if (ano == 0):
    ano = date.today().year


if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é BISEXTO'.format(ano))
else:
    print( 'O ano {} não é BISEXTO'.format(ano))