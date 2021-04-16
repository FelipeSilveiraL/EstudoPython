funcionario = str(input('Qual é o nome do Funcionario: '))

salarioAtual = float(input('Qual é o salário do {} ? R$'.format(funcionario)))

porcentagem = float(input('Qual é a % do aumento: '))

salarioAumentado = salarioAtual + (salarioAtual * porcentagem) / 100

print('O funcionario {} que ganhava R$ {:.2f}, com {}% de aumento, passa a receber R$ {:.2f}'.format(funcionario, salarioAtual, porcentagem, salarioAumentado))