# -----------------------------------------------
#    EXERCÍCIO 86
# -----------------------------------------------

matriz = [[], [], []]
for i in range(0, 3):
    for c in range(0, 3):
        num = int(input('Digite um valor para [{}, {}]: '.format(i, c)))
        matriz[i].append(num)
print('-='*20)
for i in range(0, 3):
    for n in matriz[i]:
        print(f'[ {n} ]', end= '')
    print('')
