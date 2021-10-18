#Laço de repetição FOR

#contagem crescente
for a in range(0, 7):
    print(a)
print('Fim')

#contagem decrecente
for b in range(7, 0, -1):
    print(b)
print('Fim')

#contagem multiplas
for c in range(0, 8, 2):
    print(c)
print('Fim')

#contagem usando input do usuário
n = int(input("Vamos contar, digite um numero: "))

for d in range(0, n+1):
    print(d)
print('FIM da contagem!')

#somando utilizando input do usuário
s = 0
for e in range(0, 4):
    usuario = int(input('Digite um valor: '))
    s += usuario # += é a memsa coisa que s = s+n
print('O somatório de todos os valores foi {}'.format(s))