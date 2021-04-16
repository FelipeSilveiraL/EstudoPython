#
# Aula  6 exercicio 3
# 

nome = str(input('olá desconhecido, me fale o seu nome para iniciarmos: '))

print("Seja bem vindo {}".format(nome))

n1 = int(input('Vamos dividir? -- Digite um numero: '))

print('{}'.format(n1))

n2 = int(input('Certo, agora escolha um outro numero: '))

soma = n1 / n2

print('Divisão de {} mais o {} é {}'.format(n1, n2, soma))

#
# Aula  6 exercicio 4 
# 

v = input('Digite algo: ')

print('tipo primitivo deste valor é: ', type(v))

print('só tem espaço ?', v.isspace())

print('é um numero ?', v.isnumeric())

print('é alfabetico ?', v.isalpha())

print('é alfanumerico ?', v.isalnum())

print('esta em maiusculo ?', v.isupper())

print('esta em minusculo ?', v.islower())

print('esta capitalizada ?', v.istitle()) #nem maiuscula e nem minuscula