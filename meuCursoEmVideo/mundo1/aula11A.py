##CORES poadrão ANCI

#-> \033[   style, text, background    m


#style -> negrito, etc.
#text -> a cor do texto
#back -> cor do fundo

# ex: \033[0;33;44m

#style -> 0{none}, 1{bold}, 4{underline}, 7{negative}
#text -> 30{branco}, 31{vermelho}, 32{verde}, 33{amarelo}, 34{azul}, 35{magenta}, 36{ciano}, 37{cinza}
#background ->40{branco}, 41{vermelho}, 42{verde}, 43{amarelo}, 44{azul}, 45{magenta}, 46{ciano}, 47{cinza}

print('\033[2;35mOlá, mundo!\033[m')


a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))