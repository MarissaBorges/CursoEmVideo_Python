# -----------------------------------------------
#    EXERCÍCIO 102
# -----------------------------------------------

def fatorial(n, show=False):
    if show == False:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(f'{c} = ' if c == 1 else f'{c} x ', end='')
        return f




print(fatorial(2, True))