import java.util.Scanner;

public class Inversion{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("ingrese una palabra");
		String frase = input.nextLine();
		for(int i = frase.length()-1 ;i >= 0;i--){
			System.out.print(frase.substring(i,i+1));
		}
	}
}