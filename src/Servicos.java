public class Servicos {
    public static Processo[] inicializar(int qtde){
        Processo[] processos = new Processo[qtde];
        int maior = -1;
        for(int i = 0; i<qtde; i++){
            if(i == 0 || processos[i-1].coordenador < i){
                maior = i;
            }
            processos[i] = new Processo(i, maior);
        }
        return processos;
    }

    public static void simular_falha(int id, Processo[] processos){
        processos[id].ativo = false;
    }


}
