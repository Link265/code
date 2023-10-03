import javax.swing.*;
import java.awt.event.*;

public class Eventos2 extends JFrame implements ActionListener{
	JButton button1,button2,button3;
	JLabel label1;
	public Eventos2(){
		setLayout(null);
		

		button1 = new JButton("1");
		button1.setBounds(25,100,50,20);
		add(button1);
		button1.addActionListener(this);

		button2 = new JButton("2");
		button2.setBounds(100,100,50,20);
		add(button2);
		button2.addActionListener(this);

		button3 = new JButton("3");
		button3.setBounds(175,100,50,20);
		add(button3);
		button3.addActionListener(this);

		label1 = new JLabel("hola");
		label1.setBounds(30,40,300,50);
		add(label1);
	}
	public void actionPerformed(ActionEvent e){
		
		if(e.getSource() == button1){
			label1.setText("Usted esta en la seccion 1");
		}
		if(e.getSource() == button2){
			label1.setText("Usted esta en la seccion 2");
		}
		if(e.getSource() == button3){
			label1.setText("Usted esta en la seccion 3");
		}
	}
	public static void main(String arg[]){
		Eventos2 even = new Eventos2();
		even.setBounds(0,0,300,200);
		even.setVisible(true);
		even.setLocationRelativeTo(null);
	}
}