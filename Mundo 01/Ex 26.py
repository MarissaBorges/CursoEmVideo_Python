# -----------------------------------------------
#    EXERCÍCIO 26
# -----------------------------------------------
frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" aparece {} vezes na sua frase'.format(frase.count('a')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('E aparece a última vez na posição {}'.format(frase.rfind('a')+1))
