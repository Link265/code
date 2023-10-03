import javax.swing.*;//libreria de interfaz grafica
import java.awt.event.*; // libreria de eventos de click y casillas

public class CampoDeTexto extends JFrame implements ActionListener{
	JLabel label1;

	JTextField textfield;

	JButton button1;

	public CampoDeTexto(){
		setLayout(null);

		label1 = new JLabel("usuario");
		label1.setBounds(10,10,70,30);
		add(label1);

		textfield = new JTextField();
		textfield.setBounds(100,10,150,30);
		add(textfield);

		button1 = new JButton("aceptar");
		button1.setBounds(10,80,100,30);
		add(button1);
		button1.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button1){
			String text = textfield.getText();
			setTitle(textfield.getText());//esta funcion establece el titulo
		}
	}
	public static void main(String arg[]){
		CampoDeTexto campo = new CampoDeTexto();
		campo.setBounds(0,0,400,200);
		campo.setVisible(true);
		campo.setResizable(false);
		campo.setLocationRelativeTo(null);
	}
}
