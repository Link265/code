//Checkbox1
import javax.swing.*;
import javax.swing.event.*;

public class Checkbox1 extends JFrame implements ChangeListener{
	private JCheckBox casilla1 = new JCheckBox("1");
	private JCheckBox casilla2 = new JCheckBox("2");
	private JCheckBox casilla3 = new JCheckBox("3");

	public Checkbox1(){
		setLayout(null);

		casilla1.setBounds(10,10,70,25);
		casilla1.addChangeListener(this);
		add(casilla1);

		casilla2.setBounds(10,50,70,25);
		casilla2.addChangeListener(this);
		add(casilla2);

		casilla3.setBounds(10,90,70,25);
		casilla3.addChangeListener(this);
		add(casilla3);
	}

	public void stateChanged(ChangeEvent e){
		String a = "";
		if(casilla1.isSelected() == true){
			a = a + "1-";
		}
		if(casilla2.isSelected() == true){
			a = a + "2-";
		}
		if(casilla3.isSelected() == true){
			a = a + "3-";
		}
		setTitle(a);
	}
	public static void main(String[] args){
		Checkbox1 box = new Checkbox1();
		box.setBounds(0,0,400,300);
		box.setVisible(true);
		box.setLocationRelativeTo(null);
	}
}