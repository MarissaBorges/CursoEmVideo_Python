# -----------------------------------------------
#    EXERCÍCIO 18
# -----------------------------------------------

from math import radians, sin, cos, tan


an = float(input('Digite o valor de um ângulo: '))
num = radians(an)

sen = sin(num)
cos = cos(num)
tan = tan(num)

print('O Seno desse ângulo é: {:.2f}'.format(sen))
print('O Cosseno desse ângulo é: {:.2f}'.format(cos))
print('E a Tangente desse ângulo é: {:.2f}'.format(tan))
