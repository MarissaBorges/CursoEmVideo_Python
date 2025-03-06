# -----------------------------------------------
#    EXERCÍCIO 53
# -----------------------------------------------
fra = str(input('Digite uma frase:{} '.format('\033[32m'))).strip().upper()
lista = fra.split()
frase = ''.join(lista)
fraaoCon = frase[::-1]

print('{}A frase {} no mundo invertido seria {}'.format('\033[m', frase, fraaoCon))
if frase == fraaoCon:
    print('Essa frase é um {}palíndromo{}'.format('\033[34m', '\033[m'))
else:
    print('Essa frase não é um palíndromo')
