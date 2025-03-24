# -----------------------------------------------
#    EXERCÍCIO 95
# -----------------------------------------------
    
jogadores = []
    
while True:
    dados = {}
    gols = []
    tot = 0
    nome = str(input('Nome do Jogador: '))
    dados['Nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(1, partidas + 1):
            gol = int(input(f'Quantos gols na partida {c}? '))
            gols.append(gol)
            tot += gol
    dados['Gols'] = gols[:]
    dados['Total'] = tot
    jogadores.append(dados.copy())
        
    v = str(input('Quer continuar? [S/N] ')).lower().strip()
    while v not in 'sn':
        v = str(input('Quer continuar? [S/N] ')).lower().strip()
    if v == 'n':
        break
    print('-=' * 30)
    
print('-=' * 30)
print(f'{"Cod":<3} {"Nome":<10} {"Gols":<20} {"Total":<5}')
print('-' * 42)
for p, j in enumerate(jogadores):
    print(f'{p:<3} {j["Nome"]:<10} {str(j["Gols"]):<20} {j["Total"]:<5}')
print('-' * 42)

while True:
    cod = int(input('Mostrar dados de qual jogador? '))
    if cod == 999:
        break
    if cod > len(jogadores) or cod < 0:
        cod = int(input('Mostrar dados de qual jogador? '))
    
    for p, j in enumerate(jogadores):
        if p == cod:
            print(f'-- LEVANTAMENTO DO JOGADOR {str(j["Nome"]).upper()} --')
            for p, c in enumerate(j['Gols']):
                print(f'    -> No Jogo {p + 1} fez {c} gols.')
    print('-'*40)
print('--- ENCERRADO ---')