# -----------------------------------------------
#    EXERCÍCIO 41
# -----------------------------------------------
from datetime import date
nas = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
idad = ano - nas
lim = '\033[m'
azul = '\033[1;34m'

print('Quem nasceu em {} tem {} anos e é classificado como:'.format(nas, idad))
if idad <= 9:
    print('{}MIRIM{}'.format(azul, lim))
elif idad <= 14:
    print('{}INFANTIL{}'.format(azul, lim))
elif idad <= 19:
    print('{}JUNIOR{}'.format(azul, lim))
elif idad <=20:
    print('{}SÊNIOR{}'.format(azul, lim))
else:
    print('{}MASTER{}'.format(azul, lim))
