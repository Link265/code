import javax.swing.*;//el * es para importar todas las librerias de swing
public class Interfazgrafica extends JFrame{//hereda la clase JFrame
	private JLabel label1;

	public Interfazgrafica(){
		setLayout(null); //nos permite ubicar el elemento con coordenadas
		label1 = new JLabel("hola");//declara una jlabel con un texto dentro
		label1.setBounds(100,89,30,20);//coordenadas del texto
		add(label1);//anade el texto
	}
	public static void main(String[] args) {
		Interfazgrafica gra = new Interfazgrafica();
		gra.setBounds(350,250,600,300);//coordenadaX,coordenadaY,ancho,altura
		gra.setVisible(true);//hace visible ls ventana
		gra.setResizable(false);//permite modificar el size de la ventana

		gra.setLocationRelativeTo(null);/*centra la ventana
		convierte las primeras coordenadas de setbounds a 0 0*/
	}
}