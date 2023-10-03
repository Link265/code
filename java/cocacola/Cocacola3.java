import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

public class Cocacola3 extends JFrame implements ActionListener{
	
	JMenuBar menubar = new JMenuBar();

	JMenu menu1 = new JMenu("options");
	JMenuItem newOption = new JMenuItem("Nuevo");
	JMenuItem exitOption = new JMenuItem("Salir");
	JMenu colorselect = new JMenu("Color de fondo");
	JMenuItem colorRed = new JMenuItem("Red");
	JMenuItem colorPurple = new JMenuItem("Purple");
	JMenuItem colorBlack = new JMenuItem("Black");

	JMenu menu2 = new JMenu("calculate"); 
	JMenuItem vacations = new JMenuItem("vacaciones");

	JMenu menu3 = new JMenu("about");
	JMenuItem creator = new JMenuItem("creator");


	JLabel nombreL = new JLabel("nombre completo");
	JLabel apellido1L = new JLabel("primer apellido");
	JLabel apellido2L = new JLabel("segundo apellido");

	JTextField nombre = new JTextField();
	JTextField apellido1 = new JTextField();
	JTextField apellido2 = new JTextField();

	JComboBox departament = new JComboBox();
	JLabel departamentL = new JLabel("departament");
	JComboBox timeWorked = new JComboBox();
	JLabel timeWorkedL = new JLabel("time worked");


	JLabel areaL = new JLabel("calculo de vacaciones");
	JTextArea area = new JTextArea();
	JScrollPane pane = new JScrollPane(area);

	JLabel image = new JLabel(new ImageIcon("images/logo-coca.png"));
	JLabel welcome = new JLabel("welcome");
	JLabel administratorL;
	JLabel matter = new JLabel("Datos del trabajador para el calculo de vacaciones");
	JLabel footer = new JLabel("2022 the Coca Cola Company | " +
								"Todos los derechos reservados");

	String administrator = "";


	public Cocacola3(){
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setIconImage(new ImageIcon(getClass().getResource("images/icon.png")).getImage());
		setTitle("Pantalla principal");
		getContentPane().setBackground(new Color(255,0,0));


		setJMenuBar(menubar);
		menubar.add(menu1);
		menubar.add(menu2);
		menubar.add(menu3);

		menu1.add(colorselect);
		colorselect.add(colorRed);
		colorselect.add(colorPurple);
		colorselect.add(colorBlack);
		menu1.add(newOption);
		menu1.add(exitOption);

		menu2.add(vacations);

		menu3.add(creator);

		colorBlack.addActionListener(this);
		colorPurple.addActionListener(this);
		colorRed.addActionListener(this);
		vacations.addActionListener(this);
		creator.addActionListener(this);
		exitOption.addActionListener(this);
		newOption.addActionListener(this);

		image.setBounds(5,10,250,100);
		add(image);

		Color white = new Color(255,255,255);

		welcome.setFont(new Font("Time New Roman",1,30));
		welcome.setForeground(white);
		welcome.setBounds(300,50,200,30);
		add(welcome);


		administrator = new Cocacola1().text;
		administratorL = new JLabel(administrator);
		administratorL.setFont(new Font("Time New Roman",1,30));
		administratorL.setForeground(white);
		administratorL.setBounds(450,50,200,30);
		add(administratorL);

		matter.setBounds(90,130,550,30);
		matter.setFont(new Font("Time New Roman",1,18));
		add(matter);
		matter.setForeground(white);

		nombreL.setBounds(30,180,150,20);
		nombreL.setForeground(white);
		nombreL.setFont(new Font("Time New Roman",1,10));
		add(nombreL);
		nombre.setBounds(30,200,150,20);
		add(nombre);

		apellido1L.setBounds(30,250,150,20);
		apellido1L.setForeground(white);
		apellido1L.setFont(new Font("Time New Roman",1,10));
		add(apellido1L);
		apellido1.setBounds(30,270,150,20);
		add(apellido1);

		apellido2L.setBounds(30,320,150,20);
		apellido2L.setForeground(white);
		apellido2L.setFont(new Font("Time New Roman",1,10));
		add(apellido2L);
		apellido2.setBounds(30,340,150,20);
		add(apellido2);

		departamentL.setBounds(330,180,150,20);
		departamentL.setForeground(white);
		departamentL.setFont(new Font("Time New Roman",1,10));
		add(departamentL);
		departament.setBounds(330,200,250,20);
		//departament.setBackground(white);
		add(departament);

		departament.addItem("");
		departament.addItem("Atencion al cliente");
		departament.addItem("Logistica");
		departament.addItem("Gerencia");

		timeWorkedL.setBounds(330,250,150,20);
		timeWorkedL.setForeground(white);
		timeWorkedL.setFont(new Font("Time New Roman",1,10));
		add(timeWorkedL);
		timeWorked.setBounds(330,270,250,20);
		//timeWorked.setBackground(white);
		add(timeWorked);

		timeWorked.addItem("");
		timeWorked.addItem("1 year");
		timeWorked.addItem("2 a 6 years");
		timeWorked.addItem("7 years");

		areaL.setBounds(330,320,150,20);
		areaL.setForeground(white);
		areaL.setFont(new Font("Time New Roman",1,10));
		add(areaL);
		pane.setBounds(330,340,350,100);
		add(pane);
		area.setForeground(new Color(255,0,0));
		area.setFont(new Font("Time New Roman",1,15));
		area.setText("\n\n\n   resultado del calculo de vacaciones");
		area.setEditable(false);

		footer.setBounds(90,450,600,30);
		footer.setFont(new Font("Time New Roman",1,17));
		footer.setForeground(white);
		add(footer);
	}
	public void actionPerformed(ActionEvent e){

		String tw = timeWorked.getSelectedItem().toString();
		String d = departament.getSelectedItem().toString();

		if(e.getSource() == colorRed){
			getContentPane().setBackground(new Color(255,0,0));
		}
		if(e.getSource() == colorBlack){
			getContentPane().setBackground(new Color(0,0,0));
		}
		if(e.getSource() == colorPurple){
			getContentPane().setBackground(new Color(100,0,150));
		}
		if(e.getSource() == exitOption){
			Cocacola1 co = new Cocacola1();
			co.setBounds(0,0,430,550);
			co.setVisible(true);
			co.setResizable(false);
			co.setLocationRelativeTo(null);

			this.setVisible(false);
		}	
		if(e.getSource() == newOption){
			nombre.setText("");
			apellido1.setText("");
			apellido2.setText("");

			departament.setSelectedIndex(0);
			timeWorked.setSelectedIndex(0);
			area.setText("\n\n\n   resultado del calculo de vacaciones");
		}	
		if(e.getSource() == vacations){
			String va = "";
			if(nombre.getText().equals("") || apellido1.getText().equals("") ||
			   apellido2.getText().equals("") || departament.getSelectedItem().toString().equals("")|| 
			   timeWorked.getSelectedItem().toString().equals("")){
			   JOptionPane.showMessageDialog(null,"llene todos los campos");
			}else{

				if(departament.getSelectedItem().toString().equals("Atencion al cliente")){
					if(timeWorked.getSelectedItem().toString().equals("1 year")){
						va = "6";
					}
					if(timeWorked.getSelectedItem().toString().equals("2 a 6 years")){
						va = "14";
					}
					if(timeWorked.getSelectedItem().toString().equals("7 years")){
						va = "20";
					}
				}
				if(departament.getSelectedItem().toString().equals("Logistica")){
					if(timeWorked.getSelectedItem().toString().equals("1 year")){
						va = "7";
					}
					if(timeWorked.getSelectedItem().toString().equals("2 a 6 years")){
						va = "15";
					}
					if(timeWorked.getSelectedItem().toString().equals("7 years")){
						va = "22";
					}
				}
				if(departament.getSelectedItem().toString().equals("Gerencia")){
					if(timeWorked.getSelectedItem().toString().equals("1 year")){
						va = "10";
					}
					if(timeWorked.getSelectedItem().toString().equals("2 a 6 years")){
						va = "20";
					}
					if(timeWorked.getSelectedItem().toString().equals("7 years")){
						va = "30";
					}
				}
				area.setText("el trabajador " + nombre.getText() +" "+ apellido1.getText()+" "+
							 apellido2.getText() + "\nquien labora en " + departament.getSelectedItem().toString() +" con "+
							 timeWorked.getSelectedItem().toString()+"\nde servicio "+
							 "\nrecibe "+va +" dias de vacaciones");
			}
		}
		if(e.getSource() == creator){
			JOptionPane.showMessageDialog(null,"17 years old \n" +
												"name : Fabian \n" +
												"last name : Tovar");
		}	
	}
	public static void main(String[] args){
		Cocacola3 co = new Cocacola3();
		co.setBounds(0,0,800,550);
		co.setVisible(true);
		co.setResizable(false);
		co.setLocationRelativeTo(null);
	}
}