# -----------------------------------------------
#    EXERCÍCIO 107
# -----------------------------------------------

from Ex107 import moeda

preco = float(input('Digite um preço: '))
print(f'A metade de {preco} é R$ {moeda.metade(preco):.2f}')
print(f'O dobro de {preco} é R$ {moeda.dobro(preco):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10):.2f}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(preco, 13):.2f}')