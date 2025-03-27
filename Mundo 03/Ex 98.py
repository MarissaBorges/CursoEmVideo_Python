# -----------------------------------------------
#    EXERCÍCIO 98
# -----------------------------------------------
from time import sleep

def contador(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        p = abs(p)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if i > f :
        p = (-p)
        f -= 1
    else:
        f += 1
    for c in range(i, f, p):
        print(c, end= ' ')
        sleep(0.5)
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de escolher a contagem!')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
