import javax.swing.*;
import java.awt.event.*;

public class Ejercicio1 extends JFrame implements ActionListener{

	JTextField field;
	JScrollPane pane;
	JTextArea area;
	JButton button;

	String text="";	

	public Ejercicio1(){
		setLayout(null);

		field = new JTextField();
		field.setBounds(10,10,80,30);
		add(field);

		area = new JTextArea();
		pane = new JScrollPane(area);
		pane.setBounds(10,100,400,300);
		add(pane);

		button = new JButton("Aceptar");
		button.setBounds(200,10,100,50);
		add(button);
		button.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		//if(e.getSource() == button){

			text+=field.getText() + "\n";
			field.setText("");
			area.setText(text);
			
		//}
	}
	public static void main(String[] args){
		Ejercicio1 ejer = new Ejercicio1();
		ejer.setBounds(0,0,500,450);
		ejer.setVisible(true);
		ejer.setLocationRelativeTo(null);
	}
}	
