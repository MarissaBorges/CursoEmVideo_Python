# -----------------------------------------------
#    EXERCÍCIO 15
# -----------------------------------------------
d = float(input('Quantos dias o carro ficou alugado? '))
k = float(input('Quantos Km foram rodados? '))
r = (d * 60) + (k * 0.15)

print('O valor do aluguel é igual a R${:.2f}'.format(r))
