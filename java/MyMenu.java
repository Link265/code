import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MyMenu extends JFrame implements ActionListener{
	JMenuBar menubar = new JMenuBar();
	JMenu menu = new JMenu("Opciones");
	JMenuItem item1 = new JMenuItem("red");
	JMenuItem item2 = new JMenuItem("green");
	JMenuItem item3 = new JMenuItem("blue");

	public MyMenu(){
		setLayout(null);

		setJMenuBar(menubar);

		menubar.add(menu);

		menu.add(item1);
		item1.addActionListener(this);

		menu.add(item2);
		item2.addActionListener(this);

		menu.add(item3);
		item3.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		Container co = this.getContentPane();
		if(e.getSource() == item1){
			co.setBackground(new Color(255,0,0));
		}
		if(e.getSource() == item2){
			co.setBackground(new Color(0,255,0));
		}
		if(e.getSource() == item3){
			co.setBackground(new Color(0,0,255));
		}
	}
	public static void main(String[] args){
		MyMenu menu = new MyMenu();
		menu.setBounds(0,0,300,200);
		menu.setVisible(true);
		menu.setLocationRelativeTo(null);
	}
}