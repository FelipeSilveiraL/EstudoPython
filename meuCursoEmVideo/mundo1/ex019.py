import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
n5 = str(input('Quinto Aluno: '))

alunos = [n1, n2, n3, n4, n5]

escolhido = random.choice(alunos)

print('Aluno sorteado é {}'.format(escolhido))