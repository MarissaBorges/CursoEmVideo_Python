# -----------------------------------------------
#    EXERCÍCIO 99
# -----------------------------------------------
from time import sleep

def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end= ' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores no total')
    if len(num) == 0:
        print('O maior valor foi 0')
    else:
        print(f'O maior valor foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
