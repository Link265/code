import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Cocacola1 extends JFrame implements ActionListener{

	private JLabel labelImage;
	private JLabel labelinformation = new JLabel("Vacational Control System");
	private JLabel nombre = new JLabel("insert your name:");
	private JLabel year = new JLabel("2022 Cocacola");

	private JTextField field = new JTextField();

	private JButton agreed = new JButton("Accept");

	public static String text = "";

	public Cocacola1(){
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setTitle("Welcome");
		getContentPane().setBackground(new Color(250,0,0));
		setIconImage(new ImageIcon(getClass().getResource("images/icon.png")).getImage());

		ImageIcon myimage = new ImageIcon("images/logo-coca.png");
		labelImage = new JLabel(myimage);
		labelImage.setBounds(80,90,260,100);
		add(labelImage);

		labelinformation.setBounds(80,200,300,25);
		labelinformation.setFont(new Font("Times New Roman",3,14));
		labelinformation.setForeground(new Color(250,250,250));
		add(labelinformation);

		nombre.setBounds(80,250,200,20);
		nombre.setFont(new Font("Times New Roman",3,18));
		nombre.setForeground(new Color(250,250,250));
		add(nombre);

		field.setBounds(80,275,250,25);			

							//("fuente",tipo de letra,size)
							//tipos 0 = normal
								//	1 = negrta | 2 = cursiva | 3 = cursiva negrita
		field.setFont(new Font("Times New Roman",3,14));
		field.setBackground(new Color(200,200,200));
		field.setForeground(new Color(250,0,0));
		add(field);

		agreed.setBounds(161,320,100,20);
		agreed.setBackground(new Color(200,200,200));
		agreed.setForeground(new Color(250,0,0));
		agreed.addActionListener(this);
		add(agreed);

		year.setBounds(140,500,200,20);
		year.setFont(new Font("Times New Roman",3,18));
		year.setForeground(new Color(250,250,250));
		add(year);
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == agreed){
				text = field.getText().trim();
			if (text.equals("")) {
				JOptionPane.showMessageDialog(null,"ingrese su nombre");
			}else{
				Cocacola2 cola = new Cocacola2();
				cola.setBounds(0,0,600,400);
				cola.setVisible(true);
				cola.setResizable(false);
				cola.setLocationRelativeTo(null);

				this.setVisible(false); 
			}
		}	
			
	}
	public static void main(String[] args){
		Cocacola1 co = new Cocacola1();
		co.setBounds(0,0,430,550);
		co.setVisible(true);
		co.setResizable(false);
		co.setLocationRelativeTo(null);
	}
}