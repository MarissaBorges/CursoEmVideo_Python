# -----------------------------------------------
#    EXERCÍCIO 94
# -----------------------------------------------

pessoa = {}
grupo = []
sidade = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).lower().strip()
    while pessoa['Sexo'] not in 'mf':
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).lower().strip()
    pessoa['Idade'] = int(input('Idade: '))
    sidade += pessoa['idade']
    v = str(input('Quer continuar? [S/N] ')).lower().strip()
    while v not in 'sn':
        v = str(input('Quer continuar? [S/N]: ')).lower().strip()
    grupo.append(pessoa.copy())
    if v == 'n':
        break


media = sidade/len(grupo)
print('-='*20)
print(f'-- O grupo tem {len(grupo)} pessoas.')
print(f'-- A média de idade é de {media} anos')
print(f'-- As mulheres cadastradas foram: ', end= '')
for p in grupo:
    for c in p:
        if c == 'Sexo' and p[c] == 'f':
            print(p['Nome'], end=', ')
print()

print('\nLista das pessoas que estão acima da média de idade:')
for p in grupo:
    for c in p:
        if c == 'Idade' and p[c] > media:
            for l in p:
                print(f'{l} = {p[l]};', end= ' ')
            print()
            print()

print('<< ENCERRADO >>')
