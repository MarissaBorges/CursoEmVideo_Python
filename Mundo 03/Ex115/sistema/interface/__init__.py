from time import sleep

# cores
limpo = '\033[m'
amarelo = '\033[33m'
azul = '\033[34m'
verde = '\033[32m'
vermelho = '\033[31m'

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o valor.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    sleep(1)
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{amarelo}{c}{limpo} - {azul}{item}{limpo}')
        c += 1
    linha()
    resposta = leiaint(f'{verde}Sua opção: {limpo}')
    return resposta
    