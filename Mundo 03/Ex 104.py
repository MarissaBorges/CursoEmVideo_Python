# -----------------------------------------------
#    EXERCÍCIO 104
# -----------------------------------------------

def leiaint(msg):
    print('-'*30)
    while True:
        n = input(msg)
        if not n.isnumeric():
            print('\033[31mERRO! Digite um valor válido.\033[m')
        else:
            return n

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')