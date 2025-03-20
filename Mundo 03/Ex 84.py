# -----------------------------------------------
#    EXERCÍCIO 84
# -----------------------------------------------

pessoas = []
dado = []
maior_peso = menor_peso = 0
c = 0
while True:
    c += 1
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if c == 1:
        maior_peso = menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    ver = str(input('Deseja continuar? [S/N] ')).lower()
    while ver not in 'sn':
        ver = str(input('Deseja continuar? [S/N] ').lower())
    if ver == 'n':
        break

print('-='*20)
print(f'Foram cadastratads {len(pessoas)} pessoas.')
print('As pessoas mais pesadas foram: ', end= '')
for p in pessoas:
    if p[1] == maior_peso:
        print(p[0], end= ' ')
print(f'Com {maior_peso} Kg.')
print('\n As pessoas mais leves foram: ', end= '')
for p in pessoas:
    if p[1] == menor_peso:
        print(p[0], end= ' ')
print(f'Com {menor_peso} Kg.')
