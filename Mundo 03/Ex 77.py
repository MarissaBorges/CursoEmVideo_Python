# -----------------------------------------------
#    EXERCÍCIO 77
# -----------------------------------------------
palavras = ('AMOR', 'TRISTEZA', 'PENSAMENTOS', 'DINOSSAURO', 'PYTHON', 'LIQUIDIFICADOR', 'ARMA', 'TENIS', 'JOGOS', 'COMPUTADOR', 'DESEMPREGADO')

for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c]} temos ', end = '')
    for l in palavras[c]:
        if l.lower() in 'aeiou':
            print(l.lower(), end = ' ')
    print()
print()
