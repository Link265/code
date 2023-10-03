import javax.swing.*;
import java.awt.event.*;

public class Ev extends JFrame implements ActionListener{
	private JButton button1;
	public Ev(){
		setLayout(null);
		button1 = new JButton("cerrar");
		button1.setBounds(20,10,100,30);
		add(button1);
		button1.addActionListener(this);

	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button1){
			System.exit(0);
		}
	}
	public static void main(String args[]){
		Ev event = new Ev();
		event.setBounds(0,0,500,500);
		event.setVisible(true);
		event.setResizable(false);
		event.setLocationRelativeTo(null);
	}
}