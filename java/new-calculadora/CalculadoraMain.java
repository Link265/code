import java.util.Scanner;
public class CalculadoraMain{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
  	 	System.out.println("ingrese el primer valor");
  	 	int a = input.nextInt();
  	 	System.out.println("ingrese el segundo valor");
  	 	int b = input.nextInt();

  	 	Suma suma = new Suma(a,b);

  	 	suma.prin();
	}
}