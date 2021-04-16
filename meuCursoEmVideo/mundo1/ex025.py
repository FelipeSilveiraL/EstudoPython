str = str(input('Digite seu nome e vamos valida-lo: ')).strip()

nome = str.lower()

tem = nome.count('silva')

print('Seu nome tem silva ? {}'.format((tem == 1)))