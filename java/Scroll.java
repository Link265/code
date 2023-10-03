import javax.swing.*;

public class Scroll extends JFrame{
	private JTextArea textarea1;
	private JScrollPane scrollPane;
	public Scroll(){
		setLayout(null);
		textarea1 = new JTextArea();
		scrollPane = new JScrollPane(textarea1);
		scrollPane.setBounds(10,10,200,200);
		add(scrollPane);
	}
	public static void main(String args[]){
		Scroll scroll = new Scroll();
		scroll.setBounds(0,0,300,300);
		scroll.setVisible(true);
		scroll.setLocationRelativeTo(null);
	}
}