# -----------------------------------------------
#    EXERCÍCIO 50
# -----------------------------------------------
print('Escolha 6 números')
s = 0
for c in range(1, 7):
    num = int(input('Número {}: '.format(c)))
    if num % 2 == 0:
        s += num
print('A soma dos valores pares é igual a {}'.format(s))\
