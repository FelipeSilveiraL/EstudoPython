from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2)

print('Vamos jogar ?')
print(
    '[0] Pedra\n'
    '[1] papel\n'
    '[2] Tesoura\n'
)
jogador = int(input('Escolha sua opção: '))
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('po')
time.sleep(1)
print('-=' * 11)
print('Computador escolheu: {}'.format(itens[computador]))
print('Você escolheu: {}'.format(itens[jogador]))
print('-=' * 11)

if (jogador == computador):
    print('\033[33mEmpate\033[m')
elif (jogador == 0 and computador == 1):
    print('\033[31mPERDEU\033[m')
elif (jogador == 0 and computador == 2):
    print('\033[32mVENCEU\033[m')
elif (jogador == 1 and computador == 0):
    print('\033[32mVENCEU\033[m')
elif (jogador == 1 and computador == 2):
    print('\033[31mPERDEU\033[m')
elif (jogador == 2 and computador == 0):
    print('\033[31mPERDEU\033[m')
elif (jogador == 2 and computador == 1):
    print('\033[32mVENCEU\033[m')
else:
    print('Jogada INVALIDA')