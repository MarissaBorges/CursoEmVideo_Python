# -----------------------------------------------
#    EXERCÍCIO 60
# -----------------------------------------------
num = int(input('informe um número: '))

print('{}! = '.format(num), end='')
print(num, end='')
for c in range(num, 1, -1):
    print(' x {}'.format(c-1),end='')
    num = num * (c-1)
print(' = {}'.format(num))
