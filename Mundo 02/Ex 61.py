# -----------------------------------------------
#    EXERCÍCIO 61
# -----------------------------------------------
num = int(input('Informe o primeiro termo da PA: '))
raz = int(input('Informe a razão da PA: '))
c = 1

print('\nOs 10 primeiros termos dessa razão são: ')
print(num, end = ' ')
while c < 10 :
    print(num + raz, end = ' ')
    num += raz
    c += 1
print('\n')
