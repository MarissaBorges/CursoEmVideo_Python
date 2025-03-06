# -----------------------------------------------
#    EXERCÍCIO 59
# -----------------------------------------------
from time import sleep

lim = '\033[m'
azul = '\033[1;34m'
roxo = '\033[35m'
verd = '\033[32m'
verm = '\033[31m'

num1 = int(input('{}Digite o primeiro valor: '.format(lim)))
num2 = int(input('Digite o segundo valor: '))
print('')
print('''Informe o que deseja fazer com esses valores:
[1] {}Somar{}
[2] {}Multiplicar{}
[3] {}Maior{}
[4] {}Novos números{}
[5] {}Sair do programa{}'''.format(roxo,lim, roxo, lim, roxo, lim, verd, lim, verm, lim))
print('{}'.format(lim))
op = int(input('Sua escollha: {}'.format(azul)))

while op != 5:
    if op == 1:
        print('{}A soma dos valores {} e {} é igual a {}'.format(lim, num1, num2, (num1+num2)))
        print('{}'.format(lim))
        op = int(input('O que deseja fazer agora?{} '.format(azul)))
    elif op == 2:
        print('{}A multiplicação dos termos {} e {} é igual a {}'.format(lim, num1, num2, (num1*num2)))
        print('{}'.format(lim))
        op = int(input('O que deseja fazer agora?{} '.format(azul)))
    elif op == 3:
        if num1 > num2:
            print('{}O maior valor é {}'.format(lim, num1))
        else:
            print('{}O maior valor é {}'.format(lim, num2))
        print('{}'.format(lim))
        op = int(input('O que deseja fazer agora?{} '.format(azul)))
    elif op == 4:
        num1 = int(input('{}Qual o primeiro valor novo?{} '.format(lim, azul)))
        num2 = int(input('{}Qual o segundo valor novo?{} '.format(lim, azul)))
        op = int(input('{}O que deseja fazer com esses valores?[1/2/3/4/5]{} '.format(lim, azul)))

print('')
print('{}Fechando o programa...{}'.format(verm, lim))
sleep(1)
