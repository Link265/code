import javax.swing.*;
import java.awt.event.*;

public class Suma extends JFrame implements ActionListener{
	JButton button;
	JTextField field1;
	JTextField field2;
	JLabel resultado;

	public Suma(){
		setLayout(null);

		JLabel valor1 = new JLabel("valor 1");
		valor1.setBounds(100,35,50,20);
		add(valor1);

		JLabel valor2 = new JLabel("valor 2");
		valor2.setBounds(100,75,50,20);
		add(valor2);

		resultado = new JLabel("resultado:");
		resultado.setBounds(150,130,150,30);
		add(resultado);

		field1 = new JTextField();
		field1.setBounds(160,30,80,30);
		add(field1);

		field2 = new JTextField();
		field2.setBounds(160,70,80,30);
		add(field2);

		button = new JButton("sumar");
		button.setBounds(10,100,70,30);
		add(button);
		button.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){

		int num1 = Integer.parseInt(field1.getText());
		int num2 = Integer.parseInt(field2.getText());
		int num3 = num1 + num2;

		if(e.getSource() == button){
			resultado.setText("resultado:"+num3);
		}
	}
	public static void main(String[] args){
		Suma suma = new Suma();
		suma.setBounds(0,0,400,200);
		suma.setVisible(true);
		suma.setLocationRelativeTo(null);
	}
}