# -----------------------------------------------
#    EXERCÍCIO 113
# -----------------------------------------------

def leiaint(msg):
    print('-'*30)
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o valor\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        else:
            return n
        
def leiafloat(msg):
    print('-'*30)
    while True:
        try:
            n = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o valor\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número real válido.\033[m')
            continue
        else:
            return n

i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {i} e o número real {r}')
