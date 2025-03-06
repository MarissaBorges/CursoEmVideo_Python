# -----------------------------------------------
#    EXERCÍCIO 29
# -----------------------------------------------
vel = int(input('Qual a velocidade do seu carro? '))
if vel > 80:
    mul = (vel - 80)*7
    print('Você foi multado, pois ultrapassou a velocidade maxima de 80km/h e terá que pagar {} reais'.format(mul))
else:
    print('Você não ultrapassou a velocidade maxima de 80km/h.')
