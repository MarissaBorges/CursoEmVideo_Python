# -----------------------------------------------
#    EXERCÍCIO 91
# -----------------------------------------------

from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = []
print('Valores sendo sorteados...')
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)

ranking = sorted(jogos.items(), key=itemgetter(1) , reverse= True)
print('-=' * 20)
print('== Ranking dos Jogadores ==')

for p, v in enumerate(ranking):
    print(f'    - {p + 1}° lugar: Jogador {v[0]} com {v[1]}')
    sleep(0.8)
