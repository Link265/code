import javax.swing.*;
import java.awt.event.*;//libreria de eventos de combox

public class Combo extends JFrame implements ItemListener{

	JComboBox combo;
	public Combo(){
		setLayout(null);

		combo = new JComboBox();
		combo.setBounds(10,10,100,25);
		add(combo);

		combo.addItem("rojo");
		combo.addItem("azul");
		combo.addItem("amarillo");

		combo.addItemListener(this);
	}
	public void itemStateChanged(ItemEvent e){
		if(e.getSource() == combo){
			setTitle(combo.getSelectedItem().toString());
		}
	}
	public static void main(String[] args){
		Combo box = new Combo();
		box.setBounds(0,0,200,100);
		box.setVisible(true);
		box.setLocationRelativeTo(null);
	}
}
