str = str(input('Digite um nome da sua Cidade: ')).strip()

cidade = str.upper()

cidadePadrao = "CURITIBA"

if cidade[:8] != cidadePadrao:
    print('Cidade que tenho aqui cadastrada não confere com o que vc informou')
else:
    print('é a sua cidade!')

