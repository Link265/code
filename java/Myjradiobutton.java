import javax.swing.*;
import javax.swing.event.*;

public class Myjradiobutton extends JFrame implements ChangeListener{
	JRadioButton radio1 = new JRadioButton("opcion1");
	JRadioButton radio2 = new JRadioButton("opcion2");
	JRadioButton radio3 = new JRadioButton("opcion3");

	ButtonGroup group = new ButtonGroup();
	public Myjradiobutton(){
		setLayout(null);

		radio1.setBounds(10,10,100,25);
		add(radio1);
		radio1.addChangeListener(this);
		group.add(radio1);

		radio2.setBounds(10,50,100,25);
		add(radio2);
		radio2.addChangeListener(this);
		group.add(radio2);

		radio3.setBounds(10,90,100,25);
		add(radio3);
		radio3.addChangeListener(this);
		group.add(radio3);
	}
	public void stateChanged(ChangeEvent e){
		if(radio1.isSelected()){
			setSize(250,150);
		}
		if(radio2.isSelected()){
			setSize(350,200);
		}
		if(radio3.isSelected()){
			setSize(400,300);
		}
	}
	public static void main(String args[]){
		Myjradiobutton m = new Myjradiobutton();
		m.setBounds(0,0,400,300);
		m.setVisible(true);
		m.setLocationRelativeTo(null);
	}
}