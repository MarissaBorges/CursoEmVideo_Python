# -----------------------------------------------
#    EXERCÍCIO 103
# -----------------------------------------------

def ficha(nome='<desconhecido>', gols=0):
    jogador = str(input('Nome do Jogador: '))
    gol = input('Número de Gols: ')
    if jogador != '':
        nome = jogador
    if gol.isnumeric():
        gols = gol
    
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    

print('-'*30)
print(ficha())