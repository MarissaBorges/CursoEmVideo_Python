# -----------------------------------------------
#    EXERCÍCIO 28
# -----------------------------------------------
from random import randint
from time import sleep
limpa = '\033[m'
num = randint(0, 5)
print('{}-={}'.format('\033[33m', limpa) * 30)
print('{}Vou pensar em um número entre 0 e 5, tente adivinhar...{}'.format('\033[34m', limpa))
print('{}-={}'.format('\033[33m', limpa) * 30)
user = int(input('Em que número eu pensei? \033[33m'))
print('{}PROCESSANDO...{}'.format('\033[36m', limpa))
sleep(3)
print('Eu pensei no número {}{}{} e o seu número foi {}{}{}'.format('\033[32m', num, limpa, '\033[31m', user, limpa))
if num == user:
    print('{}Parabéns!!! Você adivinhou o número.{}'.format('\033[32m', limpa))
else:
    print('{}Não foi dessa vez, tente novamente{}'.format('\033[31m', limpa))
