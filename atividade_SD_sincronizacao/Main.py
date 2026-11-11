import Processo
import Servicos

processos = Servicos.inicializar(int(input("Digite a quantidade de processos: ")))
for i in range(len(processos)):
    print(f"ID: {processos[i].id} | Coordenador: {processos[i].coordenador} | Ativo: {processos[i].ativo}")
proc = int(input("Digite o processo para falhar: "))
Servicos.simular_falha(proc, processos)
print(f"ID: {processos[proc].id} | Coordenador: {processos[proc].coordenador} | Ativo: {processos[proc].ativo}")
num = int(input("Digite o processo para começar a eleição: "))

for i in range(num, len(processos)):
    processos[i].coordenador = 3


for i in range(num, len(processos)):
    Servicos.eleicao_valentao(processos, i)

Servicos.imprimir_mensagens()
for i in range(len(processos)):
    if processos[i].ativo:
        print(f"Novo coordenador: P{processos[i].coordenador+1}")
        break




"""
for i in range(num, len(processos)):
    Servicos.eleicao_valentao(processos, num)

Servicos.imprimir_mensagens()
for i in range(len(processos)):
    if processos[i].ativo:
        print(f"Novo coordenador: P{processos[i].coordenador+1}")
        break
"""


