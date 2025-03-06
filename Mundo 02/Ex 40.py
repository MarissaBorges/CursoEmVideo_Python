# -----------------------------------------------
#    EXERCÍCIO 40
# -----------------------------------------------
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
lim = '\033[m'

if media <= 5.0:
    print('{}REPROVADO!!{}'.format('\033[1;31m',lim))
elif 5.0 <= media <= 6.9:
    print('{}RECUPERAÇÃO!!{}'.format('\033[1;33m',lim))
elif media >= 7.0:
    print('{}APROVADO!!{}'.format('\033[1;32m',lim))
