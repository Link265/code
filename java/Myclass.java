public class Myclass{
	public static void main(String args[]) {
		//*entetos*
		byte bite= 108;// -128 hasta 127
		short todoroki= 3400;// -32,768 hasta 32,767
		int integral= 140000000;// -2,147,483,648 hasta -2,147,483,648
		long largo= 999399999;//muy grande

		//*decimales*
		float flota = 2500.49;//decimales peque;os (little)
		
		double doble = 24.335333333;//decimales  grandes (long)
		
		//*caracteres*
		char cha = 'h';

		//*boleanos*
		boolean bol = true;
		

		System.out.println("byte:"+bite);
		System.out.println("short:"+todoroki);
		System.out.println("int:"+integral);
		System.out.println("long:"+largo);
		System.out.println("float:"+flota);
		System.out.println("double:"+doble);
		System.out.println("char:"+cha);
		System.out.println("boolean:"+bol);

		System.out.println(cha);

	}
}
