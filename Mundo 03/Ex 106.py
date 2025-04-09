# -----------------------------------------------
#    EXERCÍCIO 106
# -----------------------------------------------

from time import sleep

limpo = '\033[m'
fundo_branco = '\033[7m'
fundo_azul = '\033[30;44m'
fundo_verde = '\033[30;42m'
fundo_vermelho = '\033[30;41m'

def pyhelp(func=0):
    print(limpo)
    while True:
        # Mensagem inicial com fundo verde
        msg_inicial = '  SISTEMA DE AJUDA PyHELP  '
        print(fundo_verde, end='')
        print('~' * len(msg_inicial))
        print(msg_inicial)
        print('~' * len(msg_inicial), limpo)

        # Entrada do usuário
        func = str(input('("fim" para sair) Função ou Biblioteca -> '))

        if func.lower() == 'fim':
            # Mensagem final com fundo vermelho
            msg_final = '  ATÉ LOGO  '
            print(fundo_vermelho, end='')
            print('-' * len(msg_final), limpo)
            print(msg_final)
            print('-' * len(msg_final), limpo)
            break

        # Mensagem de acesso ao manual com fundo azul
        msg_manual = "  Acessando o manual do comando '{func}'  "
        print(fundo_azul, end='')
        print('~' * len(msg_manual))
        print(msg_manual)
        print('~' * len(msg_manual), limpo)
        sleep(1)

        # Exibe o manual com fundo branco
        print(fundo_branco, end='')
        help(func)
        print(limpo)
        

pyhelp()