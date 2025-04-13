def moeda(num):
    return (f'R${num:.2f}')

def aumentar(p, v, f=False):
    p = p + (p * v / 100)
    if f:
        p = moeda(p)
    return p

def diminuir(p, v, f=False):
    p = p - (p * v / 100)
    if f:
        p = moeda(p)
    return p

def dobro(p, f=False):
    p = p * 2
    if f:
        p = moeda(p)
    return p

def metade(p, f=False):
    p = p / 2
    if f:
        p = moeda(p)
    return p

def tabela(msg, preco):
    print(f'{msg:<20}', end='')
    print(f'{preco:<10}')

