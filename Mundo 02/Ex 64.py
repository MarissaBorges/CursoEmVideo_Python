# -----------------------------------------------
#    EXERCÍCIO 64
# -----------------------------------------------

l = 1
c = 0
s = 0
while l != 999:
    num = int(input('Digite um valor: '))
    if num == 999:
        l = 999
    c += 1
    s += num

print('\nVocê digitou {} valores e a soma deles é igual a {}'.format(c, s-999))
