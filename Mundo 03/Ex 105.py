# -----------------------------------------------
#    EXERCÍCIO 105
# -----------------------------------------------

def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não mostrar a situação geral da turma.
    :return: um dicionario com várias informações sobre a situação da turma.
    '''
    turma = {}
    total = maior = menor = media = s = 0
    for pos, c in enumerate(num):
        s += c
        if pos == 0:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    
    total = len(num)
    media = s / total
    if media > 7:
        situacao = 'BOA'
    elif media < 6:
        situacao = 'RUIM'
    else:
        situacao = 'RAZOÁVEL'
    
    turma['total'] = total
    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = media

    if sit:
        turma['situação'] = situacao
        return turma
    else:
        return turma


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
help(notas)