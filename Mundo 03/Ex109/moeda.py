def aumentar(p=0, v=0, f=False):
    p = p + (p * v / 100)
    return p if not f else moeda(p)

def diminuir(p=0, v=0, f=False):
    p = p - (p * v / 100)
    return p if not f else moeda(p)

def dobro(p=0, f=False):
    p = p * 2
    return p if not f else moeda(p)

def metade(p=0, f=False):
    p = p / 2
    return p if not f else moeda(p)

def moeda(num=0, moeda='R$'):
    return (f'{moeda}{num:.2f}').replace('.', ',')