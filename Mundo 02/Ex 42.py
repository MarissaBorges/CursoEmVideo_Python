# -----------------------------------------------
#    EXERCÍCIO 42
# -----------------------------------------------
l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o último lado: '))
azul = '\033[36m'
lim = '\033[m'

if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
    tri = True
    print('As retas PODEM formar um triângulo')
    if l1 == l2 == l3:
        print('Esse é um triângulo do tipo {}EQUILÁTERO{}'.format(azul, lim))
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Esse é um triângulo do tipo {}ISOSCELES{}'.format(azul, lim))
    elif l1 != l2 != l3 != l1:
        print('Esse é um triângulo do tipo {}ESCALENO{}'.format(azul,lim))

else:
    tri = False
    print('As retas NÃO podem formar um triângulo')
