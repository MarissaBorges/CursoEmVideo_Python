# -----------------------------------------------
#    EXERCÍCIO 69
# -----------------------------------------------
a = h = m = 0

while True:
    id = int(input('Informe a idade: '))
    sx = str(input('Qual o sexo? [M/F] ')).strip().lower()[0]
    while sx not in 'mf':
        sx = str(input('O valor é INVÁLIDO! Informe um valor [M/F]: ')).strip().lower()[0]

    if id > 18:
        a += 1
    if sx == 'm':
        h += 1
    if sx == 'f' and id < 20:
        m += 1

    print('Dados registrados com sucesso!\n')
    q = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while q not in 'sn':
        q = str(input('Valor INVÁLIDO.\nDeseja continuar? \nInforme Sim[S] ou Não[n]: ')).strip().lower()[0]
    if q == 'n':
        break
print(f'\nNos registros existem {a} pessoas maiores de 18 anos.\n{h} Homens e {m} Mulheres com menos de 20 anos')
