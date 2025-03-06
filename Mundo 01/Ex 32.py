# -----------------------------------------------
#    EXERCÍCIO 32
# -----------------------------------------------
from datetime import date
ano = int(input('Para analisar o ano atual digite 0, senão informe um ano: '))
anoB = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
if ano == 0:
    ano = date.today().year # Pega o ano atual da máquina
if anoB == 0:
    print('Esse é um ano Bissexto')
else:
    print('Esse não é um ano Bissexto')
