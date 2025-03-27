# -----------------------------------------------
#    EXERCÍCIO 96
# -----------------------------------------------

def area(l, c):
    s = l * c
    return s

print('     Controle de terrenos')
print('-' * 20 )
a = float(input('Largura: (m) '))
b = float(input('Comprimento: (m) '))

print(f'A área do terreno de {a} x {b} é de {area(a, b)}m²')
