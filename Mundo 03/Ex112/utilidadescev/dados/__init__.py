def LeiaDinheiro(msg):
    while True:
        num = input(msg).replace(',', '.').strip()
        if num.replace('.', '', 1).isdigit():
            valor = float(num)
            break
        else:
            print(f'\033[31mERRO: "{num}" é um preço inválido!!\033[m')
    return valor

def resumo(valor, porc1, porc2):
    from Ex112.utilidadescev.moeda import tabela, dobro, moeda, aumentar, metade, diminuir
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)

    tabela('Preço analisado:', moeda(valor))
    tabela('Dobro do preço:', dobro(valor, True))
    tabela('Metade do preço:', metade(valor, True))
    tabela(f'{porc1}% de aumento:', aumentar(valor, porc1, True))
    tabela(f'{porc2}% de redução', diminuir(valor, porc2, True))
    print('-'*30)
