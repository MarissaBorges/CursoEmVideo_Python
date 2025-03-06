#------------------------------------------------
#    EXERCÍCIO 20
# -----------------------------------------------

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lt = [a1, a2, a3, a4]
random.shuffle(lt)
print('A ordem sorteada foi \n{}'.format(lt))
