# -----------------------------------------------
#    EXERCÍCIO 94
# -----------------------------------------------

pessoa = {}
grupo = []
sidade = 0
while True:
    nome = str(input('Nome: '))
    pessoa['Nome'] = nome
    sexo = str(input('Sexo [M/F]: ')).lower().strip()
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).lower().strip()
    pessoa['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['Idade'] = idade
    sidade += idade
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
