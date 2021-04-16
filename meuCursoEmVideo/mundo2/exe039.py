from datetime import datetime

data = datetime.now()
idadeAlistamento = 18


print('Vamos saber está chegando ou passou o seu dia do Alistamento Militar')
print('*-*' * 20)

anoUsuario = int(input('Qual é o ano do seu nascimento? '))

""" Sabendo qual é a idadade do usuáio """
idadeUsuario = data.year - anoUsuario

if data.year >= anoUsuario:
    if idadeAlistamento >= idadeUsuario:

        """Calculo"""
        anosFatante = idadeAlistamento - idadeUsuario

        aindafalta = anosFatante + data.year

        print('Você tem {}anos, ainda falta {}anos, seu alistamento será em {}'.format(
            idadeUsuario, anosFatante, aindafalta))

    elif idadeUsuario == idadeAlistamento:
        print('Você tem {}anos, então chegou o ano do seu Alistamento. Procure uma junta militar e faça o seu cadastro'.format(idadeUsuario))
    else:

        """Calculo"""
    anosPassados = idadeUsuario - idadeAlistamento
    passou = data.year - anosPassados

    print('Você tem {}anos, então passou {}anos do o seu alistamento foi {}'.format(
        idadeUsuario,anosPassados, passou))
else:
    print('O ano que você informou é maior que o ano que estamos. Isso quer dizer que vc ainda não nasceu!')