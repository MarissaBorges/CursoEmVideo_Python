# -----------------------------------------------
#    EXERCÍCIO 83
# -----------------------------------------------
p1 = []
p2 = []
expressao = str(input('Digite uma expressão: ')).strip()

for c in expressao:
    if c == '(':
        p1.append(c)
    elif c == ')':
        p2.append(c)

if len(p1) == len(p2):
    print('A sua expressao esta correta')
else:
    print('A sua expressao esta INCORRETA')
