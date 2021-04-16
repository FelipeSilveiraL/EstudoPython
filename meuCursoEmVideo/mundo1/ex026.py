str = str(input('Digite um nome para saber quntas letras A possui: ')).strip()

print('A letra A apareceu pela primeira vez na posição {}'.format(str.lower().find('a')+1))

print('A letra A aparece {} vezes na frase'.format(str.lower().count('a')))

print('A letra A apareceu a última vez foi {}'.format(str.lower().rfind('a')+1))