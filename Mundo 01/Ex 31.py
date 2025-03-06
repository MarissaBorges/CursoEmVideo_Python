# -----------------------------------------------
#    EXERCÍCIO 31
# -----------------------------------------------
dist = int(input('Qual a distância da viagem? '))
if dist > 200:
    print('Sua viagem vai custar {:.0f} reais'.format(dist*0.50))
else:
    print('Sua viagem vai custar {:.0f} reais'.format(dist*0.45))
