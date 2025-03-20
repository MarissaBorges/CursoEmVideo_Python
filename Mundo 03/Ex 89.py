# -----------------------------------------------
#    EXERCÍCIO 89
# -----------------------------------------------

geral = []
nome = []
nota = []

while True:
    nome.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    nome.append(nota[:])
    media = (nota[0] + nota[1]) /2
    nome.append(media)
    geral.append(nome[:])
    nome.clear()
    nota.clear()
    v = str(input('Deseja continuar? [S/N] ')).lower()
    while v not in 'sn':
        v = str(input('Deseja continuar? [S/N]')).lower()
    if v == 'n':
        break

print('-='*20)
print('{:<}{:^10}{:>12}'.format('No.', 'NOME', 'MEDIA'))
print('-'*25)
for c in range(0, len(geral)):
    print(f'{c:<}', end= '     ')
    print(f'{geral[c][0]}', end= '     ')
    print(f'{geral[c][-1]:>12}')
print('-'*30)

while True:
    c = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if c == 999:
        break
    print(f'Notas de {geral[c][0]} são {geral[c][1]}')
    print('-'*30)
print('FINALIZANDO...')
