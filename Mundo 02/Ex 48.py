# -----------------------------------------------
#    EXERCÍCIO 48
# -----------------------------------------------
print('Todos os números ímpares que são multiplos de 3 no intervalo entre 1 e 500 são:')
con = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        con += 1
        s += c
print('Existem {} valores e a soma total é: {}'.format(con, s))
