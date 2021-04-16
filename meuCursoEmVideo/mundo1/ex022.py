nome = str(input('Digite o seu nome: ')).strip() #.strip() -> é para cortar os espaços antes e depois da palavra

print('Seu nome em Maiusculo é {}'.format(nome.upper()))

print('Seu nome em minuscula é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #-nome.count(' ') -> isso é para elimiar os espaços entre as palavras

separaNome = nome.split()

print('Seu primeiro nome é {} e tem {} letras'.format(separaNome[0], len(separaNome[0])))