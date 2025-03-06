# -----------------------------------------------
#    EXERCÍCIO 62
# -----------------------------------------------
num = int(input('Qual o primeiro termo da PA? '))
raz = int(input('Qual a razão da PA: '))

c = 1
c2 = 10
print('\nOs 10 primeiros termos dessa PA são: ')

while c != c2:
    print(num, end = ' ')
    while c < c2 :
        print(num + raz, end = ' ')
        num += raz
        c += 1

    c2 = int(input('\n \nDeseja ver mais quantos termos? '))
    if c2 == 0:
        c = c2+1
    else:
        c = 1
