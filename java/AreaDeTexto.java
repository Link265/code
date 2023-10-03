import javax.swing.*;//libreria de interfaz grafica

public class AreaDeTexto extends JFrame{
	public AreaDeTexto(){
		setLayout(null);
		JTextArea textArea = new JTextArea();
		textArea.setBounds(10,10,200,200);
		add(textArea);
	}
	public static void main(String[] args){
		AreaDeTexto area = new AreaDeTexto();
		area.setBounds(0,0,500,500);
		area.setVisible(true);
		area.setLocationRelativeTo(null);
	}
}
