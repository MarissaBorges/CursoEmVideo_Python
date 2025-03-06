# -----------------------------------------------
#    EXERCÍCIO 23
# -----------------------------------------------
n = int(input('Escolha um número entre 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('unidades: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhar: {}'.format(m))
