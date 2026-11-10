import Processo

def inicializar(qtde):
    processos = []
    maior = -1
    for i in range(int(qtde)):
        if maior < i:
            maior = i
        processos.append(Processo.Processo(i, maior))
    return processos

def simular_falha(i, processos):
    processos[i].ativo = False

def eleicao_valentao(processos, x):





"""
ideias:
    -pra fazer o loop em anel usar um while que dá break quando i chegar na posição inicial da lista
    -criar duas arraylists em cada processo, uma de mensagens enviadas e outra de recebidas
    -no início de cada eleição, apagar as arrays de mensagens de todos os processos
"""

