# -----------------------------------------------
#    EXERCÍCIO 112
# -----------------------------------------------
from Ex112.utilidadescev import moeda
from Ex112.utilidadescev import dados

p = dados.LeiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
