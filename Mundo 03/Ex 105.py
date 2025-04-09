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
    turma['total'] = len(num)
    turma['maior'] = max(num)
    turma['menor'] = min(num)
    turma['media'] = sum(num) / len(num)

    if sit:
        if turma['media'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['media'] < 6:
            turma['situação'] = 'RUIM'
        else:
            turma['situação'] = 'RAZOÁVEL'
    
    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print()
help(notas)