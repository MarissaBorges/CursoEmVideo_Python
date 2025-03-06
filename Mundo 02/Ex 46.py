# -----------------------------------------------
#    EXERCÍCIO 46
# -----------------------------------------------
from time import sleep
print('{:=^60}'.format(' Contagem Regressiva ')) 
#Escreve o texto centralizado ('^') em uma cadeia de caracteres
#Entre um caracter ('=')

print('')

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('')
print('Feliz Ano Novoo!!!')
