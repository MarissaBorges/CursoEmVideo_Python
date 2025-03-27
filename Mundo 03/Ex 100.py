# -----------------------------------------------
#    EXERCÍCIO 100
# -----------------------------------------------
from random import randint
from time import sleep

numeros = []

def sortear():
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        num = randint(1, 20)
        print(num, end= ' ')
        numeros.append(num)
        sleep(0.7)
    print('PRONTO!!')

def somarPar():
    print(f'Somando os valores pares de {numeros},', end= ' ')
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'temos {s}')

sortear()
somarPar()