# -----------------------------------------------
#    EXERCÍCIO 81
# -----------------------------------------------
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    v = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while v not in 'sn':
        v = str(input('Valor inválido! quer continuar? [S/N] ')).strip().lower()[0]
    if v == 'n':
        break
print('-='*20)
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('5 não se encontra na lista')
