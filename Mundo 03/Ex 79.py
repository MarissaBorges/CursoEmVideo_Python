# -----------------------------------------------
#    EXERCÍCIO 79
# -----------------------------------------------
valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado, não vou adicioná-lo!')
    else:
        valores.append(num)
        print('Valor registrado!')
    c = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while c not in 'sn':
        c = str(input('Valor inválido, quer continuar? [S/N] '))
    if c == 'n':
        break
print('-='*20)
print(f'Você digitou os valores {sorted(valores)}')
