# -----------------------------------------------
#    EXERCÍCIO 70
# -----------------------------------------------
# 50, 20, 10, 1
from time import sleep
c = v = d = u = 0
print('BEM-VINDO ao caixa eletrônico da CAIXA\n')
valor = int(input('Qual o valor a ser sacado? '))
print('PROCESSANDO')
sleep(1)
while True:
    if valor == 0:
        break
    if (valor // 50) >= 1:
        c += 1
        valor -= 50
    else:
        if (valor // 20) >= 1:
            v += 1
            valor -= 20
        else:
            if (valor // 10) >= 1:
                d += 1
                valor -= 10
            else:
                u = valor
                valor = 0
print(f'Você receberá {c} notas de R$50, {v} notas de R$20, \n{d} notas de R$10 e {u} notas de R$1.')
