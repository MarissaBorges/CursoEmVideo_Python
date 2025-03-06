# -----------------------------------------------
#    EXERCÍCIO 76
# -----------------------------------------------
#39 e 32
c = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9) 

print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)

for d in range(0,len(c),2):
    print('{:.<30}R$'.format(c[d]), end='')
    print('{:>7.2f}'.format(c[d+1]))
print('-'*40)
