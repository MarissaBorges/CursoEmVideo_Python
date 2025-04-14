def aumentar(p=0, v=0):
    p = p + (p * v / 100)
    return p

def diminuir(p=0, v=0):
    p = p - (p * v / 100)
    return p

def dobro(p=0):
    p = p * 2
    return p

def metade(p=0):
    p = p / 2
    return p

def moeda(num=0, moeda='R$'):
    return (f'{moeda}{num:.2f}').replace('.', ',')