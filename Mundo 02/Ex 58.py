# -----------------------------------------------
#    EXERCÍCIO 58
# -----------------------------------------------
from random import randint
from time import sleep

lim = '\033[m'
azul = '\033[34m'
verm = '\033[31m'
verd = '\033[32m'
azulN = '\033[1;34m'
roxo = '\033[35m'
comp = randint(0, 10)
print('{}{:=^70}'.format(lim, ' {}TENTE ADIVINHAR{} '.format(roxo,lim)))
sleep(0.5)
print('{}PENSANDO....'.format(lim))
print('')

print('Acabei de pensar em um número entre {}0{} e {}10{} tente acertar qual foi...'.format(verd, lim, verd, lim))
num = int(input('Sua escolha: {}'.format(azulN)))
sleep(1)
print('{}...'.format(lim))
sleep(0.5)
print('')
c = 1

while num != comp:
    print('{:-^70}'.format(' {}° Tentativa '.format(c+1)))
    print('Você {}ERROOOU{}!!'.format(verm, lim))
    if comp > num:
        print('O seu valor é menor...')
    elif comp < num:
        print('O seu número é maior...')
    num = int(input('Tente novamente:{} '.format(azulN)))
    print('{}'.format(lim))
    c += 1
    sleep(1)
print('{}{}PARABÉNSSSSS{}!!! Você conseguiu acertar'.format(lim, verd, lim))
print('Precisou de {}{}{} tentativa(s) para isso'.format(verd, c, lim))
