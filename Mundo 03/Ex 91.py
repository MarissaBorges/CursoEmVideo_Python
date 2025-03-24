# -----------------------------------------------
#    EXERCÍCIO 91
# -----------------------------------------------

from random import randint
from time import sleep
primeiro = segundo = terceiro = quarto = 0
ranking = {}
print('Valores sendo sorteados...')
for c in range(1, 5):
    ranking[f"Jogador {c}"] = randint(1,6)
    print(f'O jogador {c} tirou {ranking[f"Jogador {c}"]}')
    sleep(0.8)

print('Ranking dos Jogadores')
for c in range(0,1):
    primeiro = segundo = terceiro = quarto = ranking['Jogador 1']
    for k in ranking.keys():
        if ranking[k] > primeiro:
            primeiro = k
        if ranking[k] > segundo:
            segundo = k
        if ranking[k] > terceiro:
            terceiro = k
        if ranking[k] < quarto:
            quarto = k

for c in range (1, 5):
    print(f'{c}° lugar: Jogador {c} com {ranking[f"Jogador {c}"]}')
    sleep(0.8)
