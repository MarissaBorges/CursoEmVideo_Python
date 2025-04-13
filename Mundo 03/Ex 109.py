# -----------------------------------------------
#    EXERCÍCIO 109
# -----------------------------------------------

from Ex109 import moeda

preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é R$ {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é R$ {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(preco, 13, True)}')