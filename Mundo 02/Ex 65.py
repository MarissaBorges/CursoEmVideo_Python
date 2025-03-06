# -----------------------------------------------
#    EXERCÍCIO 65
# -----------------------------------------------
lim = '\033[m'
verm = '\033[31m'
c = 0
l = 1
s = 0
ma = 0
me = 0

while l != 999:
    while l != 999:
        num = int(input('Digite um valor: '))
        c += 1
        s += num
        if num == 999:
            l = 999
            num = me
        if l == 1 :
            ma = num
            me = num
            l = 2
        else:
            if num > ma:
                ma = num
            if num < me:
                me = num
    print('{}\n[DESCONSIDERANDO O FLAG]{}'.format(verm, lim))
    print('A Média dos valores é igual a {}'.format((s-999)/(c-1)))
    print('O maior valor é {} e o menor é {}'.format(ma, me))
    l = str(input('\nDeseja escrever novos valores? [S/N] ')).lower()
    if l == 's':
        c = 0
        s = 0
        l = 1
    else:
        l = 999
