import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Mysubmenu extends JFrame implements ActionListener{

	JMenuBar menubar = new JMenuBar();
	JMenu menu1 = new JMenu("options");
	JMenu menu2 = new JMenu("resolution");
	JMenu menu3 = new JMenu("color");
	JMenuItem item1 = new JMenuItem("640 x 360");
	JMenuItem item2 = new JMenuItem("480 x 320");

	JMenuItem itemcolorblue = new JMenuItem("blue");
	JMenuItem itemcolorgreen = new JMenuItem("green");

	public Mysubmenu(){
		setLayout(null);

		setJMenuBar(menubar);

		menubar.add(menu1);

		menu1.add(menu2);

		menu2.add(item1);
		item1.addActionListener(this);

		menu2.add(item2);
		item2.addActionListener(this);

		menu1.add(menu3);

		menu3.add(itemcolorblue);
		itemcolorblue.addActionListener(this);
		menu3.add(itemcolorgreen);
		itemcolorgreen.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){

		if(e.getSource() == item1){
			setSize(640,360);
		}

		if(e.getSource() == item2){
			setSize(480,320);
		}
		if(e.getSource() == itemcolorgreen){
			getContentPane().setBackground(new Color(0,255,0));
		}
		if(e.getSource() == itemcolorblue){
			getContentPane().setBackground(new Color(0,0,255));
		}
	}
	public static void main(String[] args){
		Mysubmenu sub = new Mysubmenu();
		sub.setBounds(0,0,400,500);
		sub.setVisible(true);
		sub.setResizable(false);
		sub.setLocationRelativeTo(null);
	}
} 