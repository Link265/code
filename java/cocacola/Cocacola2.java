import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.awt.*;

public class Cocacola2 extends JFrame implements ActionListener,ChangeListener{
	private JLabel title = new JLabel("Terminos y condiciones");
	private JLabel coca = new JLabel(new ImageIcon("images/coca-cola.png"));

	private JTextArea area = new JTextArea();

	private JScrollPane pane = new JScrollPane(area);

	private JRadioButton radio = new JRadioButton("aceptar terminos y condiciones");

	private JButton button1 = new JButton("Siguiente");
	private JButton button2 = new JButton("No acepto");

	public Cocacola2(){
		setLayout(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setTitle("Licencia de uso");
		setIconImage(new ImageIcon(getClass().getResource("images/icon.png")).getImage());

		title.setBounds(180,20,200,30);
		title.setFont(new Font("Times New Roman",1,15));
		add(title);

		area.setText("\n\n terminos y condiciones"+ 
					"\n A primera declaracion");
		area.setEditable(false);
		pane.setBounds(10,60,570,200);
		add(pane);

		button1.setBounds(10,330,120,30);
		add(button1);
		button1.setEnabled(false);
		button1.addActionListener(this);

		button2.setBounds(160,330,120,30);
		add(button2);
		button2.addActionListener(this);

		radio.setBounds(15,270,250,20);
		add(radio);
		radio.addChangeListener(this);

		coca.setBounds(330,230,230,150);
		add(coca);
	}
	public void stateChanged(ChangeEvent e){
		if(radio.isSelected()){
			button1.setEnabled(true);
			button2.setEnabled(false);
		}else{
			button1.setEnabled(false);
			button2.setEnabled(true);
		}

		
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource() == button1){
			Cocacola3 co = new Cocacola3();
			co.setBounds(0,0,800,550);
			co.setVisible(true);
			co.setResizable(false);
			co.setLocationRelativeTo(null);

			this.setVisible(false);
		}

		if(e.getSource() == button2){
			Cocacola1 co = new Cocacola1();
			co.setBounds(0,0,430,550);
			co.setVisible(true);
			co.setResizable(false);
			co.setLocationRelativeTo(null);
		

			this.setVisible(false);
		}
	}
	public static void main(String[] args){
		Cocacola2 cola = new Cocacola2();
		cola.setBounds(0,0,600,400);
		cola.setVisible(true);
		cola.setResizable(false);
		cola.setLocationRelativeTo(null); 
	}
}
