# -----------------------------------------------
#    EXERCÍCIO 80
# -----------------------------------------------
print('Coletando 5 valores...')
lista = []
for c in range(0, 5):
    num = int(input('Informe um valor: '))
    if c == 0:
        lista.append(num)
        print('Primeiro valor adicionado ao final da lista...')
    else:
        for pos, v in enumerate(lista):
            if num < v:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
        else:
            lista.append(num)
            print('Adicionado ao final da lista...')
print(f'Os valores que você forneceu são: {lista}')
