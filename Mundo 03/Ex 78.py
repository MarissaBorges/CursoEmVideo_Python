# -----------------------------------------------
#    EXERCÍCIO 78
# -----------------------------------------------
valores = []
Pmaior = []
Pmenor = []

for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print('-='*30)

maior = max(valores)
menor = min(valores)
print(f'Os valores informados foram: {valores}')

for v in valores:
    if v == maior:
        Pmaior.append(valores.index(v)+1)
    if v == menor:
        Pmenor.append(valores.index(v)+1)

if valores.count(maior) > 1:
    print(f'O maior valor é {maior} nas posições', end= ' ')
    for n in Pmaior:
        print(n, end='... ')
else:
    print(f'O maior valor é {maior} na {valores.index(maior)}ª posição')

if valores.count(menor) > 1:
    print(f'E o menor valor é {menor} nas posições', end= ' ')
    for n in Pmenor:
        print(n, end= '... ')
else:
    print(f'E o menor valor é {menor} na {valores.index(menor)}ª posição')
