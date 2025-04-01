# -----------------------------------------------
#    EXERCÍCIO 100
# -----------------------------------------------
from random import randint
from time import sleep

def sortear(lista):
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(num, end= ' ')
        lista.append(num)
        sleep(0.7)
    print('PRONTO!!')

def somarPar(lista):
    print(f'Somando os valores pares de {lista},', end= ' ')
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'temos {s}')

numeros = []
sortear(numeros)
somarPar(numeros)