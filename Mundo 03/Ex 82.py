# -----------------------------------------------
#    EXERCÍCIO 82
# -----------------------------------------------
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    v = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while v not in 'sn':
        v = str(input('Valor Inválido, que continuar? [S/N] '))
    if v == 'n':
        break
print('-='*20)

pares = []
impares = []
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'A lista completa é {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
