# -----------------------------------------------
#    EXERCÍCIO 54
# -----------------------------------------------
from datetime import date
a = 0
for c in range(0, 7):
    nasc = int(input('Data de nascimento {}: '.format(c+1)))
    if date.today().year - nasc >= 21:
        a = a + 1
print('Das datas informadas {} atingiram a maioridade'.format(a))
