# -----------------------------------------------
#    EXERCÍCIO 38
# -----------------------------------------------
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('informe o segundo número: '))
limpo = '\033[m'

if num1 > num2:
    print('O {}primeiro valor{} é maior'.format('\033[34m', limpo))
elif num2 > num1:
    print('O {}segundo valor{} é maior'.format('\033[31m', limpo))
else:
    print('{}Os dois valores são iguais{}'.format('\033[1;32m',limpo))
