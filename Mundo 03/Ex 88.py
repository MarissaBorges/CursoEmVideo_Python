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
    for n in range(0, 6):
        num = randint(0, 60)
        if n == 0 or num not in jogo:
            jogo.append(num)
    valores.append(jogo[:])
    jogo.clear()
print('{:-^40}'.format(f' SORTEANDO {i} JOGOS '))

for c in range(0, i):
    print(f'Jogo {c + 1}: {valores[c]}')
    sleep(0.5)
print('{:=^40}'.format(' < BOA SORTE! > '))
