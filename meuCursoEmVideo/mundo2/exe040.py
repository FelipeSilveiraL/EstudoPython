#TITULO#
print("Passou, Reprovou ou está de Recuperação ?")
print("-*-"*20)

#Recebendo dados dos usuário#
notaUm = float(input("Insira nota da primeira prova = "))
notaDois = float(input("Insira nota da segunda prova = "))

#Calulando Média#
resultadoMedia = (notaUm + notaDois) / 2

#dados dos status#
aprovado = 7.0
recuperacao = 6.9
reprovado = 5.0

#aplicando a regra#

if (resultadoMedia >= aprovado):

    print('sua nota foi {}, então você foi \033[32m APROVADO\033[m'.format(resultadoMedia))

elif (resultadoMedia == recuperacao or resultadoMedia >= reprovado):

    print('sua nota foi {}, então você está de \033[33m RECUPERAÇÂO\033[m'.format(resultadoMedia))

elif (resultadoMedia < reprovado):
    
    print('sua nota foi {}, então você está \033[31m REPROVADO\033[m'.format(resultadoMedia))

#FIM#