import javax.swing.*; //libreria de interfaz grafica
import java.awt.event.*;// libreria de eventos  de click y casillas
//import java.util.Scanner;//libreria de inputs

public class Calculadora extends JFrame implements ActionListener{

	String a = "";
	int quantities[] = new int[20];

	String[] quantitiesStrin = new String[20];
	int current_quantity = 0;

	JLabel result = new JLabel("");

	JButton[] buttons = new JButton[10];
	JButton[] operadoresB = new JButton[10];
	JButton equal = new JButton("=");
	JButton delete = new JButton("DEL");

	String[] operadoresS = {"+","-","/","x"};

	String[] operacion = new String[20];

	public Calculadora(){
		setLayout(null);//permite definir el tamano de los elementos
		setDefaultCloseOperation(EXIT_ON_CLOSE);

		short x = 0;
		short y = 0;
		int size = 41;
		for(int t = 1;t<10 ; t++){
			String j = String.valueOf(t);
			buttons[t] = new JButton(j);
			buttons[t].setBounds(70+size*x,100+size*y,size,size);
			add(buttons[t]);
			buttons[t].addActionListener(this);
			x++;
			if(x > 2){
				x=0;
				y++;
			}
		}
		delete.setBounds(size*3+70,100,size*2,size);
		add(delete);
		delete.addActionListener(this);
		for (int i = 0;i < quantitiesStrin.length ;i++) {
			quantitiesStrin[i] = "";
		}
		for (int i = 0;i < operacion.length ;i++) {
			operacion[i] = "";
		}

		buttons[0]= new JButton("0");
		buttons[0].setBounds(70+size*1,100+size*3,size,size);
		add(buttons[0]);
		buttons[0].addActionListener(this);

		result.setBounds(30,70,300,22);
		add(result);

		for (int i = 0;i < 4;i++) {
			operadoresB[i] = new JButton(operadoresS[i]);
			operadoresB[i].setBounds(50+size*i,280,size,size);
			add(operadoresB[i]);
			operadoresB[i].addActionListener(this);
		}
		equal.setBounds(50+size*4,280,size,size);
		add(equal);
		equal.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		boolean still = true;

		String output = "";


		//number input
		for (int i = 0;i < buttons.length ;i++ ) {
			if(e.getSource() == buttons[i] && quantitiesStrin[current_quantity].length() < 10){

				if(operacion[current_quantity] != ""){
					current_quantity++;
				}
				quantitiesStrin[current_quantity] += buttons[i].getText().toString();
				quantities[current_quantity] =  Integer.parseInt(quantitiesStrin[current_quantity]);
				still = false;
			}
		}

		//operadores input
		for(int i = 0;i < 5 && still && quantitiesStrin[0] != "" ;i++ ){
			if(e.getSource() == operadoresB[i]){
				operacion[current_quantity] = String.valueOf(operadoresB[i].getText());
				still = false;
			}
		}

		//delete
		if(e.getSource() == delete){


			if(operacion[current_quantity] != ""){

				operacion[current_quantity] = "";

			}else if(quantitiesStrin[current_quantity] != "" && operacion[current_quantity] == ""){
				int c = quantitiesStrin[current_quantity].length();

				if(c>1){
					quantitiesStrin[current_quantity] = quantitiesStrin[current_quantity].substring(0,c-1);
					quantities[current_quantity] =  Integer.parseInt(quantitiesStrin[current_quantity]);
				}else{
					quantitiesStrin[current_quantity] = "";
					quantities[current_quantity] = 0;

					if(current_quantity > 0){
						current_quantity--;
					}
				}
			}
		}

		//draw quatities
		for(int i = 0; i < quantitiesStrin.length;i++){
			output += quantitiesStrin[i] +" " +operacion[i]+" ";
		}

		//result
		if (e.getSource() == equal && quantitiesStrin[1] != "" && still) {
			int calculate = quantities[0];
			for(int i = 0;i < quantitiesStrin.length;i++){
				if(quantitiesStrin[i+1] == ""){
					break;
				}
				if(operacion[i] == "+"){
					calculate += quantities[i+1];
				}
				if(operacion[i] == "-"){
					calculate -= quantities[i+1];
				}
				if(operacion[i] == "x"){
					calculate *= quantities[i+1];
				}
				if(operacion[i] == "/"){
					calculate /= quantities[i+1];
				}
			}
			for (int i = 0;i < quantitiesStrin.length ;i++ ){
				quantitiesStrin[i]="";
			}
			for(int i = 0;i < operacion.length;i++){
				operacion[i] = "";
			}
			current_quantity = 0;
			output = String.valueOf(calculate);
		}


		//set output
		result.setText(output);
	}
	public static void main(String[] args){
		Calculadora c = new Calculadora();
		c.setBounds(0,0,300,450);
		c.setVisible(true);
		c.setLocationRelativeTo(null);
	}
}
