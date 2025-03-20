# -----------------------------------------------
#    EXERCÍCIO 87
# -----------------------------------------------

matriz = [[], [], []]
for i in range(0, 3):
    for c in range(0, 3):
        num = int(input('Digite um valor para a posição [{}, {}]: '.format(i, c)))
        matriz[i].append(num)

print('-='*20)
pares = terc_coluna = sg_linha = 0
for i in range(0, 3):
    for p, n in enumerate(matriz[i]):
        if n % 2 == 0:
            pares += n
        if i == 1 and p == 0:
            sg_linha = n
        elif i == 1:
            if n > sg_linha:
                sg_linha = n
        if p == 2:
            terc_coluna += n
        print('[', end= '')
        print(n, end= '')
        print(']', end= '')
    print('')

print('-='*20)
print(f'A soma de todos os valores pares é igual a {pares}.')
print(f'A soma dos valores da terceira coluna é igual a {terc_coluna}.')
print(f'O maior valor da segunda linha é {sg_linha}.')
