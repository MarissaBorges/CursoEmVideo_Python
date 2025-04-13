# -----------------------------------------------
#    EXERCÍCIO 108
# -----------------------------------------------

from Ex108 import moeda

preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é R$ {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é R$ {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos R$ {moeda.moeda(moeda.diminuir(preco, 13))}')