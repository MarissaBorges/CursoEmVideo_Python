def aumentar(p, v):
    p = p + (p * v / 100)
    return p

def diminuir(p, v):
    p = p - (p * v / 100)
    return p

def dobro(p):
    p = p * 2
    return p

def metade(p):
    p = p / 2
    return p

def moeda(num):
    return (f'R${num:.2f}')