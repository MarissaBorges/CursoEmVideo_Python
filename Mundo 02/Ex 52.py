# -----------------------------------------------
#    EXERCÍCIO 52
# -----------------------------------------------
num = int(input('Informe um numero: '))

soma = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end= '')
        soma += 1
    else:
        print('\033[m', end= '')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, soma))
print('')
if soma == 2:
    print('Ele é um numero \033[34mPRIMO!\033[m')
else:
    print('Ele \033[31mNÃO\033[m é um número PRIMO!')
