def tabela(msg, preco):
    print(f'{msg:<20}', end='')
    print(f'{preco:<10}')

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

def moeda(num):
    return (f'R${num:.2f}')

def resumo(valor, porc1, porc2):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)

    tabela('Preço analisado:', moeda(valor))
    tabela('Dobro do preço:', dobro(valor, True))
    tabela('Metade do preço:', metade(valor, True))
    tabela(f'{porc1}% de aumento:', aumentar(valor, porc1, True))
    tabela(f'{porc2}% de redução', diminuir(valor, porc2, True))
    print('-'*30)
