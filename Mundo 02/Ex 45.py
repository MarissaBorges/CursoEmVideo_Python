# -----------------------------------------------
#    EXERCÍCIO 45
# -----------------------------------------------

# PROJETO DO JOGO DE JOKENPÔ

from random import choice
from time import sleep

limpo = '\033[m'
print('{}_-=-{}'.format('\033[1;35m', limpo)*20)
print('{}EU SOU PROFISSIONAL DE JOKENPÔ!!! vamos ver se você consegue ganhar de mim...{}'.format('\033[m',limpo))
print('{}_-=-{}'.format('\033[1;35m', limpo)*20)
jog = str(input('Digite "sair" para fechar o programa\nEscolha pedra/ papel/ tesoura:{} '.format('\033[32m'))).lower()

ganho = 0
perca = 0

while jog != 'sair':
    print('{}'.format(limpo))
    sleep(1.5)
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PÔ!!!')
    sleep(0.7)
    print('')
    list = ['pedra', 'papel' , 'tesoura']
    comp = choice(list)

    if jog == 'pedra' and comp == 'tesoura' or jog == 'papel' and comp == 'pedra' or jog == 'tesoura' and comp == 'papel':
        print('{}PARABÉNS!!!{} Você me venceu... \nEscolhi {}{}{} e você escolheu {}{}{}'.format('\033[1;32m', limpo, '\033[31m', comp.upper(), limpo, '\033[36m', jog.upper(), limpo))
        ganho += 1
        print('')
        jog = str(input('Quer jogar novamente? [S/N] ')).lower()
        if jog == 's':
            jog = str(input('Escolha pedra/ papel/ tesoura: {}'.format('\033[32m'))).lower()
        else:
            jog = 'sair'
    elif jog == 'pedra' and comp == 'papel' or jog == 'papel' and comp == 'tesoura' or jog == 'tesoura' and comp == 'pedra':
        print('{}HAHAHAHA!!{} Eu ganhei de você!! \nEscolhi {}{}{} e você escolheu {}{}{}'.format('\033[1;31m', limpo, '\033[36m', comp.upper(), limpo, '\033[31m', jog.upper(), limpo))
        perca += 1
        print('')
        jog = str(input('Quer jogar novamente? [S/N] ')).lower()
        if jog == 's':
            jog = str(input('Escolha pedra/ papel/ tesoura: {}'.format('\033[32m'))).lower()
        else:
            jog = 'sair'
    elif jog and comp == 'pedra' or 'papel' or 'tesoura':
        print('{}EMPATE!!{}'.format('\033[33m', limpo))
        jog = str(input('Digite "sair" para fechar ou... \nJogue um novo valor [pedra/ papel/ tesoura]:{} '.format('\033[32m'))).lower()
    else:
        print('Valor inválido!!!')
    print('')
print('')
print('{}Você perdeu {} vezes e ganhou {}'.format(limpo, perca, ganho))
print('{}Foi um prazer jogar com você{}'.format('\033[4;36m', limpo))
print('')
