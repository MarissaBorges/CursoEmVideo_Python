# -----------------------------------------------
#    EXERCÍCIO 70
# -----------------------------------------------
c = tt = pc = b = 0
while True:
    c += 1
    print('\n{:^40}'.format(f'{c} PRODUTO\n'))
    nm = str(input('Informe o nome do produto: '))
    pre = float(input('Qual o preço? '))
    tt += pre
    if pre > 1000:
        pc += 1
    if c == 1 or pre < b:
        b = pre
        nomeb = nm
    
    print(f'PRODUTO {nm.upper()} REGISTRADO\n')
    q = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while q not in 'sn':
        q = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if q == 'n':
        print('')
        break
print(f'O total gasto foi de R${tt:.2f}.\nDesses produtos {pc} custam mais de R$1.000.\nE o produto mais barato é (o/a) {nomeb.upper()}')
