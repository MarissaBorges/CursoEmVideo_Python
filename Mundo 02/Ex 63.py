# -----------------------------------------------
#    EXERCÍCIO 63
# -----------------------------------------------
n1 = int(input('Digite um número aleatório: '))
n2 = int(input('Quantos elementos da sequência de fibonacci deseja ver? '))
c = 1

e1 = n1
e2 = e1

print('\nOs {} elementos da sequencia de fibonacci são: '.format(n2))
print(e1, end='')

while c < n2:
    print(' -> {}'.format(e2), end='')
    c += 1
    s = e1 + e2
    e1 = e2
    e2 = s

print('\n')
