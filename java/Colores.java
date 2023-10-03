import javax.swing.*;
import java.awt.*;//libreria de colores
import java.awt.event.*;

public class Colores extends JFrame implements ActionListener{


	JLabel label1 = new JLabel("Red");
	JLabel label2 = new JLabel("Green");
	JLabel label3 = new JLabel("Blue");

	JComboBox box1 = new JComboBox();
	JComboBox box2 = new JComboBox();
	JComboBox box3 = new JComboBox();

	JButton button = new JButton("color");

	Color mycolor = new Color(0,200,200);

	public Colores(){
		setLayout(null);

		label1.setBounds(20,10,50,20);
		add(label1);

		label2.setBounds(20,50,50,20);
		add(label2);

		label3.setBounds(20,90,50,20);
		add(label3);

		box1.setBounds(100,10,70,20);
		add(box1);

		box2.setBounds(100,50,70,20);
		add(box2);

		box3.setBounds(100,90,70,20);
		add(box3);

		button.setBounds(170,90,80,20);
		add(button);
		button.addActionListener(this);

		for(int i = 0;i <= 255;i++){
			//convertir a string con String.valueOf(i) o i.toString()
			String a = String.valueOf(i);
			box1.addItem(a);
			box2.addItem(a);
			box3.addItem(a);
		}
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button){

			int red = Integer.parseInt(box1.getSelectedItem().toString());
			int green = Integer.parseInt(box2.getSelectedItem().toString());
			int blue = Integer.parseInt(box3.getSelectedItem().toString());

			Color col = new Color(red,green,blue);

			button.setBackground(col);
		}
	}
	public static void main(String[] args){
		Color mycolor = new Color(0,200,200);
		Colores co = new Colores();
		co.setBounds(0,0,300,150);
		co.setVisible(true);
		co.setLocationRelativeTo(null);
	}
}
