# -----------------------------------------------
#    EXERCÍCIO 95
# -----------------------------------------------
    
jogadores = []
dados = {}
gols = []
tot_gol = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    gols.clear()
    for c in range(1, partidas + 1):
            gol = int(input(f'  Quantos gols na partida {c}? '))
            gols.append(gol)
            tot_gol += gol
    dados['Gols'] = gols[:]
    dados['Total'] = tot_gol
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
    cod = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    while cod > len(jogadores) or cod < 0:
        if cod == 999:
            break
        print(f'ERRO! Não existe jogador de cod {cod}!!!')
        cod = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    if cod == 999:
        break
    
    for p, j in enumerate(jogadores):
        if p == cod:
            print()
            print(f'-- LEVANTAMENTO DO JOGADOR {str(j["Nome"]).upper()} --')
            for p, c in enumerate(j['Gols']):
                print(f'    -> No Jogo {p + 1} fez {c} gols.')
    print('-'*40)
print('--- ENCERRADO ---')
