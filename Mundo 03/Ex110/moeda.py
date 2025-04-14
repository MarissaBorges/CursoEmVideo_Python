def tabela(msg, preco=0):
    print(f'{msg:<20}', end='')   # Outra maneira seria usando o \t (tabulação) em apenas uma linha de print
    print(f'{preco:<10}')

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

def resumo(valor=0, porc1=1, porc2=1):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}') # Também poderia ser feito usando //print('RESUMO DO VALOR'.center(30))//
    print('-'*30)
    tabela('Preço analisado:', moeda(valor))
    tabela('Dobro do preço:', dobro(valor, True))
    tabela('Metade do preço:', metade(valor, True))
    tabela(f'{porc1}% de aumento:', aumentar(valor, porc1, True))
    tabela(f'{porc2}% de redução', diminuir(valor, porc2, True))
    print('-'*30)
