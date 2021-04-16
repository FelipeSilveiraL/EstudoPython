num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

if num1 > num2:
    print('O primeiro numero é \033[31mMAIOR\033[m que o segundo')
elif num2 > num1:
    print('O primeiro número é \033[32mMENOR\033[m que o segundo')
else:
    print('O primeiro número é \033[33mIGUAL\033[m ao segundo')