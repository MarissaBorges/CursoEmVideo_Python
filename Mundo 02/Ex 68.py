# -----------------------------------------------
#    EXERCÍCIO 68
# -----------------------------------------------
from random import randint
print(f"{'^-'*20}")
print("{:^40}".format('VAMOS JOGAR PAR OU ÍMPAR'))
print(f"{'^-'*20}")
c = v = 0
while True:
    com = randint(0, 10)
    n = int(input('Informe um valor: '))
    eN = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    c += 1
    if (com + n) % 2 == 0:
        r = 'par'
    else:
        r = 'impar' 
    print(f"{'-'*40}")
    print(f'Você jogou {n} e o computador {com}.\nA soma é {n+com} DEU {r.upper()}')
    print(f"{'-'*40}")
    if eN == r[0]:
        print('Você VENCEU!!')
        print('Jogue novamente...')
        print(f"{'-=':^40}")
        v += 1
    else:
        print('Você PERDEU!!')
        break
print(f'Você jogou {c} e venceu {v} vezes.')
#print('Ola' if c == 0 else '')
