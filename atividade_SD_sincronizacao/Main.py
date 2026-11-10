import Processo
import Servicos

processos = Servicos.inicializar(int(input("Digite a quantidade de processos: ")))
for i in range(len(processos)):
    print(f"ID: {processos[i].id} | Coordenador: {processos[i].coordenador} | Ativo: {processos[i].ativo}")
proc = int(input("Digite o processo para falhar: "))
Servicos.simular_falha(proc, processos)
print(f"ID: {processos[proc].id} | Coordenador: {processos[proc].coordenador} | Ativo: {processos[proc].ativo}")
print(f"ID: {processos[1].id} | Coordenador: {processos[1].coordenador} | Ativo: {processos[1].ativo}")


