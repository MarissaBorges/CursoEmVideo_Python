# -----------------------------------------------'#    EXERCÍCIO 73
# -----------------------------------------------
tabela = ('Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Santos', 'Sport', 'São Paulo', 'Vasco', 'Vitória')
chapeco = 'Chapecoense' in tabela

print(tabela)
print(f'\nOs 5 primeiros colocados são {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[16:]}')
print('\nOs times em ordem alfabética ficam:')
print(sorted(tabela))
if chapeco == True:
    chapeco = tabela.index('Chapecoense')
    print(f'\nO time da chapeco esta na posição {chapeco + 1}')
else:
    print(f'\nO time da Chapecoense não esta entre os 20 primeiros')
