num = int(input('Digite um numero inteiro: '))
print('''Esolha uma das opção abaixo: \n
[1] Converter binário
[2] Converter Octal
[3] Converter Hexadecimal \n''')

opcao = int(input('Sua opção: '))

if(opcao ==  1):
    print('{} convertido para binário é igual á {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é ihual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31m Opção \033[32m{}\033[m \033[31m inválida, Tente novamente!\033[m'.format(opcao))