import java.util.Scanner;

public class Lavadora{

	private int k;
	private String t;
	private boolean llenadoCompleto = false;
	private boolean secadoCompleto = false; 
	private boolean lavadoCompleto = false; 
	private Scanner input = new Scanner(System.in);

	public Lavadora(int kilos,int tipoDeRopa){
		this.k = kilos;
		this.t = tipoDeRopa;
	}
	public llenado(){
		if(k <= 12){
			System.out.println("llenando...");
			llenadoCompleto = true;
		}else{
			System.out.println("es demasiada ropa");
		}
	}
	public lavado(){
		
	}
	public secado(){

	}
} 