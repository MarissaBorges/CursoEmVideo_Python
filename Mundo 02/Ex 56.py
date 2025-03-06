#------------------------------------------------
#    EXERCÍCIO 56
# -----------------------------------------------
media = 0
velho = 0
nomeV = ''
cont = 0
for c in range (1, 5):
    nome = str(input('Qual o {}° nome? '.format(c))).strip()
    idade = int(input('Qual a {}° idade? '.format(c)))
    sexo = str(input('Qual o sexo da {}° pessoa? [F/M] '.format(c))).strip().upper()
    print('')
    media += idade
    media = media / c
    if sexo == 'M' and idade > velho:
        velho = idade
        nomeV = nome
    if sexo == 'F' and idade < 20:
        cont += 1

print('A média de idade do grupo foi {:.1f}'.format(media))
print('O nome do homem mais velho é o {} com {} anos'.format(nomeV, velho))
print('Existe(m) {} mulher(es) com menos de 20 anos no grupo'.format(cont))
