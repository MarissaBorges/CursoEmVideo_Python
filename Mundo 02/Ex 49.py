# -----------------------------------------------
#    EXERCÍCIO 49
# -----------------------------------------------
print('{:^40}'.format('Tabuada'))
num = int(input('Escolha um número: '))
print('A tabuada de {} é:'.format(num))

for c in range(1,11):
    print('{} x {} = {}'.format(num, c, c*num))
