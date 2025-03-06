# -----------------------------------------------
#    EXERCÍCIO 17
# -----------------------------------------------

from math import pow, sqrt

catAdj = float(input('Digite o valor do cateto adjacente: '))
catOp = float(input('Digite o valor do cateto oposto: '))

hip = sqrt((pow(catAdj, 2) + pow(catOp, 2)))

print('A hipotenusa desse triângulo retângulo é: {}'.format(hip))
