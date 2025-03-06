# -----------------------------------------------
#    EXERCÍCIO 12
# -----------------------------------------------
p = float(input('Qual o preço do produto? '))
d = p*0.05
print('O valor do desconto é R${:.2f} e o seu novo preço é R${:.2f}.'.format(d, p-d))
