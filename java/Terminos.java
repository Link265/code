import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;
public class Terminos extends JFrame implements ActionListener,ChangeListener{
	JLabel label1 = new JLabel("Terminos y condiciones");
	JCheckBox casilla1 = new JCheckBox("Aceptar");
	JButton button = new JButton("Seguir");

	public Terminos(){
		setLayout(null);

		label1.setBounds(10,10,200,25);
		add(label1);

		casilla1.setBounds(10,40,120,20);
		casilla1.addChangeListener(this);
		add(casilla1);

		button.setBounds(10,70,100,30);
		button.addActionListener(this);
		add(button);
		button.setEnabled(false);
	}
	public void stateChanged(ChangeEvent e){
		if(casilla1.isSelected() == true){
			button.setEnabled(true);
		}else{
			button.setEnabled(false);
		}
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button){
			System.exit(0);
		}
	}
	public static void main(String[] args){
		Terminos ter = new Terminos();
		ter.setBounds(0,0,300,200);
		ter.setVisible(true);
		ter.setLocationRelativeTo(null);
	}
}