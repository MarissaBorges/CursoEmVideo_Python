# -----------------------------------------------
#    EXERCÍCIO 93
# -----------------------------------------------

dados = {}
gols = []
dados['Nome'] = str(input('Nome do Jogador: '))
qua = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for c in range(1, qua+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dados['Gols'] = gols.copy()
c = 0
for v in gols:
    c += v
dados['Total'] = c

print('-='*20)
print(dados)
print('-='*20)

for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*20)
print(f'O jogador {dados["Nome"]} jogou {qua} partidas.')

for p, v in enumerate(gols):
    print(f'    => Na partida {p}, fez {v} gols.')
print(f'Foi um total de {c} gols.')
