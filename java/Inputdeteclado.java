import java.util.Scanner;//libreria de inputs

public class Inputdeteclado{

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String nombre;
		int num;
		System.out.println("what is your name?");
		nombre = input.nextLine();
		System.out.println("give me a number");
		num = input.nextInt();
		System.out.println(nombre+"       "+num);
	}


}
