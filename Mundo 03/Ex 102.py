# -----------------------------------------------
#    EXERCÍCIO 102
# -----------------------------------------------

def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.    
    '''
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} = ' if c == 1 else f'{c} x ', end='')
        f *= c
    return f

print(fatorial(5, True))
help(fatorial)
