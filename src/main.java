import java.util.Scanner;

public class main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Digite a quantidade de processos:");
        Processo[] processos = Servicos.inicializar(scan.nextInt());
        for(int i = 0; i< processos.length; i++){
            System.out.println("ID: " + processos[i].id + " Coordenador: " + processos[i].coordenador
            + " Ativo: " + processos[i].ativo);
        }
        Servicos.simular_falha(2, processos);
        System.out.println("ID: " + processos[2].id + " Coordenador: " + processos[2].coordenador
                + " Ativo: " + processos[2].ativo);
    }
}
