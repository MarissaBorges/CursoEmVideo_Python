# -----------------------------------------------
#    EXERCÍCIO 39
# -----------------------------------------------
from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
date = date.today().year
alis = date-ano

if alis < 18:
    print('Você ainda vai se alistar, falta(m) {} ano(s).'.format(18-alis))
elif alis == 18:
    print('Esta na hora de se alistar')
elif alis > 18:
    print('Já passou da sua hora de se alistar, passou(ram) {} ano(s).'.format(alis-18))
