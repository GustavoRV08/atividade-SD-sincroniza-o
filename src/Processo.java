public class Processo {
    int id;
    boolean ativo;
    int coordenador;

    public Processo(int num, int coord){
        id = num;
        ativo = true;
        coordenador = coord;
    }
}
