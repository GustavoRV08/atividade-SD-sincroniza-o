import Processo

mensagens = []

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
    existe_maior = False
    for i in range(len(processos)):
        if processos[i].ativo == True and processos[i].id > processos[x].id:
            print(f"comparação atual: {processos[i].id} > {processos[x].id}")
            mensagens.append(processos[i].receber_mensagem(processos[x].enviar_election()))
            mensagens.append(processos[x].receber_mensagem(processos[i].enviar_ok()))
            existe_maior = True
    if existe_maior == False and processos[x].ativo == True:
        print(f"id do processo atual: {processos[x].id} || estado: {processos[x].ativo}")
        for i in range(len(processos)):
            if processos[i].ativo == True and processos[i].id != processos[x].id:
                mensagens.append(processos[i].receber_mensagem(processos[x].enviar_coordinator()))

def imprimir_mensagens():
    for i in range(len(mensagens)):
        print(mensagens[i])

def teste(processos):
    if processos[3].receber_mensagem(processos[2].enviar_ok(1))[:2] == "OK":
        print(processos[3].receber_mensagem(processos[2].enviar_ok(1)))
        print("deu certo...?")



"""
ideias:
    -pra fazer o loop em anel usar um while que dá break quando i chegar na posição inicial da lista
    -criar duas arraylists em cada processo, uma de mensagens enviadas e outra de recebidas
    -no início de cada eleição, apagar as arrays de mensagens de todos os processos
    -cada processo ter funções que servem apenas para mandar mensagens
"""

