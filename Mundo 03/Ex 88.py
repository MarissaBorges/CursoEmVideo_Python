# -----------------------------------------------
#    EXERCÍCIO 88
# -----------------------------------------------
from random import randint
from time import sleep

valores = []
jogo = []

print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
i = int(input('Quantos Jogos você quer que eu sorteie? '))

for c in range(0, i):
    n = 0  # Redefine n para 0 a cada novo jogo
    while True:
        num = randint(1, 60)  # Corrige o intervalo para 1 a 60
        if num not in jogo:
            jogo.append(num)
            n += 1
        if n == 6:
            break
    valores.append(jogo[:])
    jogo.clear()

print('{:-^40}'.format(f' SORTEANDO {i} JOGOS '))

for c in range(0, i):
    print(f'Jogo {c + 1}: {sorted(valores[c])}')
    sleep(0.5)
print('{:=^40}'.format(' < BOA SORTE! > '))
