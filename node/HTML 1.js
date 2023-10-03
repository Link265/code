const canvas=document.getElementById("canvas");
const c=canvas.getContext("2d");
const size=30;

let turns=0;

let menuCharacter=false;
let cityMenu=false;
let cityResources=false;
var moveOn=false;
let productionMenu=false;

let comprobantes=[];

var currentChar=0;
var currentCity=0;
var selectUnit=false;

var selectorMenu={x:0,y:0};

let selectorAux={
	x:undefined,
	y:undefined
};

var elementos;

var characters=[];
var cities=[]; 

const selector={
	
	x:4*30,
	y:3*30,
	width:1,
	height:size,
	select:function (){
	  
		let howManyCharacters=0;
		let howManyCities=0;
	  
		characters=[];
		cities=[];
	  
	  
	  //look for character
		for(let i=0;i<character.length;i++){
		  
			if(selector.x==character[i].x&&selector.y==character[i].y){
		  
				howManyCharacters++;
				characters.push(i);
		  
			}
		}
	  
	  
	  //look for city
		for(let i=0;i<city.length;i++){
		  
		  if(selector.x==city[i].x&&selector.y==city[i].y){
			  
			  howManyCities++;
			  
			  cities.push(i);
			  
			}
		  
		}
	  
		if((howManyCharacters>1||howManyCities>1)||(howManyCharacters==1&&howManyCities==1)){
	  
			let x;
			let y;
  
  
			if(howManyCharacters>=1){
				y=character[characters[0]].y;
				x=character[characters[0]].x;
				
			}else {
				x=city[cities[0]].x;
				y=city[cities[0]].y;
			}
  
			
  
			selectorMenu.x=x;
			selectorMenu.y=y;
			selectUnit=true;
			
			

		}else{
			
			for(let a in character){
				
				if(character.length>0 && character[a].x==selector.x&&character[a].y==selector.y){
					
					character[a].menu();
					currentChar=a;
					break;
				}
				
			}
			
			for(let a in city){
				
				if(city.length>0 && selector.x==city[a].x && selector.y==city[a].y){
				
					cityMenu=true;
					currentCity=a;
					break;
					
				}
				
				
			}  
		}
	},
	back:function (){
	  this.x=character[0].x;
	  this.y=character[0].y;
  },
	selectUnitMenuDraw:function(x,y){
	  
		c.fillStyle="gray";
		c.fillRect(selectorMenu.x+size*2,selectorMenu.y-size,size*4,size*6);
		c.fillStyle="black";
		c.font="20px American Captain";
	  
		elementos=[];
	  
		for(let i=0;i<characters.length;i++){
		  
			elementos.push(character[characters[i]].name);
		  
		}
	  
		for(let i=0;i<cities.length;i++){
	
			elementos.push(city[cities[i]].name);
		}
	  
		for(let i=0;i<elementos.length;i++){
		  
			if(this.menuSelector==i){
				c.fillStyle="white";
			}else{
				c.fillStyle="black";
			}
		  
		  c.fillText(elementos[i],selectorMenu.x+size*2,selectorMenu.y+size*i);
		  
		}
		
	},
	menuSelector:0

	};	

function draw(){
	
	// limpia la pantalla para dibujar otro frame
	clean();
	
	// dibuja los personajes y ciudades
	if(!cityMenu&&!cityResources&&!productionMenu){
		
		world.drawField();
		
		const font=25;
		
		c.fillStyle="black";
		c.font=font+"px Times New Roman";
		c.fillText("turns:"+turns,canvas.width-font*5,font);
	
		for(let a of road){
			a.draw();
		}
	
		for(let i=0;i<city.length;i++){
			city[i].draw();	
		}
	
		character[0].draw();
	
		if(!menuCharacter||!selectUnit){
			drawSelector();
		}
		
	}
	if(cityMenu||productionMenu){
		
		city[currentCity].menu();
		
		
	}
	//selecciona recursos a explotar
	if(cityResources){
			city[currentCity].menu();
			drawSelector();
	}

	
	
	//abre el menu para seleccionar multiples unidades
	if(selectUnit){
		selector.selectUnitMenuDraw();
	}
	
	// dibuja menu de personaje
	if(menuCharacter){
		character[currentChar].menu();
	}
	
	// se usa cuando el persanaje se esta moviendo
	if(moveOn){
		c.fillStyle="black";
		c.font="20px American Captain";
		c.fillText(`moves:`+character[currentChar].moves,canvas.width-size*3,canvas.height-size);
	}
}	

function comparar(){
	
	if(menuCharacter||moveOn||selectUnit||cityMenu||cityResources||productionMenu){
		return false;
	}else{
		return true;
	}
}

function drawSelector(){
	
	c.fillStyle="black";
	
	//up
	c.fillRect(selector.x,selector.y,selector.height,selector.width);
	
	//left
	c.fillRect(selector.x,selector.y,selector.width,selector.height);
	
	//down
	c.fillRect(selector.x,selector.y+selector.height,selector.height,-(selector.width));
	
	//right
	c.fillRect(selector.x+selector.height,selector.y,-(selector.width),selector.height);
}

function clean(){
	
	c.clearRect(0,0,canvas.width,canvas.height);
}

function endTurn(){
	
	for(let i=0;i<character.length;i++){
		character[i].moves=character[i].initialMoves;	
	}
	
	turns++;
	
	draw();
}

class World{
	
	constructor(){
		
		this.worldArray=[];
		this.width=canvas.width;
		this.height=canvas.heigth;
	}
	
	createField(){
		
		for(let x=0;x<this.width/size;x++){
			
			this.worldArray[x]=[];
			
			for(let y=0;y<this.width/size;y++){
				
				let a=Math.floor(Math.random()*99)+1;
				
				
				
				if(a>20){
					
					this.worldArray[x][y]="greenHill";
					
					
					
				}else{
					this.worldArray[x][y]="lake";
					
				}
				
				
			}	
		}
		
	}
	
	drawField(){
		
		for(let x=0;x<this.width/size;x++){
			
			for(let y=0;y<this.width/size;y++){
				
				if(this.worldArray[x][y]=="greenHill"){
					
					c.fillStyle="green";
				}
				
				if(this.worldArray[x][y]=="lake"){
					
					c.fillStyle="blue";
				}
				
				c.fillRect(x*30,y*30,size,size);
			}	
		}
		
		
	}
}

const world = new World();
world.createField();


class City{
	
	constructor(x,y){
		this.code=city.length;
		this.x=x*size;
		this.y=y*size;
		this.name="city "+this.code;
		this.pob=100;
		this.food=0;
		this.selector=0;
		this.options=["recursos","produccion"];
		this.area=[
			[false,false,false,false,false],
			[false,false,false,false,false],
			[false,false,false,false,false],
			[false,false,false,false,false],
			[false,false,false,false,false]
		];

		this.resourcesMenu={x:11*size,y:8*size}
		this.resources=this.scanResources();
		this.productionSelector=0;
		this.products=['settler','warrior'];
	}


	scanResources(){

		let array=[];

		for(let x=0;x<5;x++){

			array[x]=[];

			for(let y=0;y<5;y++){

				array[x][y]=world.worldArray[(this.x/size)+(x-2)][(this.y/size)+(y-2)];
			}

		}
		
		return array;

	}

	menu(){
		//crea el fondo gris 
		c.fillStyle="gray";
		c.fillRect(0,0,canvas.width,canvas.height);
		
		//administrador de recursos
		c.fillStyle="white";
		
		c.fillRect(270,210,size*5,size*3);
		c.fillRect(300,180,size*3,size*5);
		
		let recursosX1=270;
		let recursosX2=300;
		
		let recursosY1=210;
		let recursosY2=180;
		
		let y2=0;
		let x2=0;
		
	
		//parte de arriba y parte de abajo
		for(let x=0;x<3;x++){
			
			if(world.worldArray[(this.x-size+size*x)/size][(this.y-size*2)/size]=="greenHill"){
				
				c.fillStyle="green";
			}
			if(world.worldArray[(this.x-size+size*x)/size][(this.y-size*2)/size]=="lake"){
				
				c.fillStyle="blue";
			}
			
			c.fillRect(recursosX2+size*x,recursosY2,size,size);
			
			//parte de abajo
			if(world.worldArray[(this.x-size+size*x)/size][(this.y+size*2)/size]=="greenHill"){
				
				c.fillStyle="green";
			}
			if(world.worldArray[(this.x-size+size*x)/size][(this.y+size*2)/size]=="lake"){
				
				c.fillStyle="blue";
			}
			
			c.fillRect(recursosX2+size*x,recursosY2+size*4,size,size);
			
		}
		
		
		
		
		//parte del medio
		for(let x=2;x>=-2;x--){
			
			for(let y=1;y>=-1;y--){
				
				if(world.worldArray[(this.x-(size*x))/size][(this.y-(size*y))/size]=="greenHill"){
					
					c.fillStyle="green";
					c.fillRect(recursosX1+size*x2,recursosY1+size*y2,size,size);
					//c.fillRect(recursosX2+size*y2,recursosY2+size*x2,size,size);
				}
				
				if(world.worldArray[(this.x-(size*x))/size][(this.y-(size*y))/size]=="lake"){
					
					c.fillStyle="blue";
					c.fillRect(recursosX1+size*x2,recursosY1+size*y2,size,size);
					//c.fillRect(recursosX2+size*y2,recursosY2+size*x2,size,size);
				}
				
				y2++;
			}
			
			y2=0;
			
			x2++;
		}
		
		//muestra la ciudad
		c.fillStyle="gray";
		c.fillRect(recursosX1+size*2,recursosY1+size,size,size);
		

		//muestra los recursos explotados

		let calculateFood=0;

		for (let x = 0;x < 5; x++) {

			for (let y=0 ; y<5 ; y++ ) {
				
				if (this.area[x][y]==true) {

					c.fillStyle='yellow';
					c.fillRect(this.resourcesMenu.x+size*(-2+x),this.resourcesMenu.y+size*(-2+y),10,10);

					if(this.resources[x][y]=='greenHill'){

						calculateFood+=2;
					}
					if(this.resources[x][y]=='lake'){

						calculateFood++;
					}
				}

			}
			
		}
		this.food=calculateFood;

		
		//muestra informacion de la ciudad
		c.fillStyle="black";
		c.font="50px Times New Roman";
		c.fillText(this.name,canvas.width/2-50,50);
		c.font="30px Times New Roman";
		
		c.fillText("pob:"+this.pob,10,size*3);
		c.fillText("food:"+this.food,size*6,size*3);

		// administrar ciudad
		
		c.fillStyle="black";
		c.font="25px Times New Roman";	
		
		for(let a in this.options){
			
			if(this.selector==a&&!productionMenu){
				
				c.fillStyle="white";
			}else{
				
				c.fillStyle="black";
			}
			
			c.fillText(this.options[a],10,size*5+a*30);
			
		}
			c.fillStyle='black';
			c.fillText('production:',10,size*8)

		for(let a in this.products){

			if(this.productionSelector==a&&productionMenu){
				c.fillStyle='white';
			}else{
				c.fillStyle='black';
			}
			c.fillText(this.products[a],10,size*9+size*a);
			
		}
		
		currentCity=this.code;
	}
	
	draw(){
		c.fillStyle="gray";
		c.fillRect(this.x,this.y,size,size);
	}

	production(){


	}
}

let city=[];

city[0]=new City(3,2);

class Character{
	
	constructor(x,y,color){
		
		this.x=x*30;
		this.y=y*30;
		this.selector=0;
		this.name="character "+character.length;
		this.wordList=["move","build city","road"];
		this.moves=2;
		this.initialMoves=2;
		
	}
	
	draw(){
		
		//draw character
		c.fillStyle="orange";
		c.fillRect(this.x,this.y,size,size);
		
	}
	
	menu(){
		
		menuCharacter=true;
		
		let menu={x:this.x,
				  y:this.y};

		if(this.y<=0){
			menu.y+=size;
		}
		
		if(this.x>canvas.width-size*7){
			menu.x-=size*7;
		}
		
		//square
		menuCharacter=true;
		c.fillStyle="gray";
		c.fillRect(menu.x+size*2,menu.y-size,size*4,size*6);
		
		//options
		
		c.font="25px Times New Roman";
		
		for(let i=0;i<this.wordList.length;i++){
			
			this.textColor(i);
			
				
			c.fillText(this.wordList[i],menu.x+size*2,menu.y+size*i);
				
			
			
		}
		
	/*	primer modelo
	    //1
	    this.textColor(0);
		
		
		c.fillText("move",this.x+size*2,this.y);
		
		//2
		this.textColor(1);
		c.fillText("build city",this.x+size*2,this.y+size);
		
		//3
		this.textColor(2);
		c.fillText("road",this.x+size*2,this.y+size*2);
		*/
		
		
		
	}
	
	textColor(a){
		
		if(this.selector==a){
			c.fillStyle="white";
		}else{
			c.fillStyle="black";
		}
		
	}
	
	move(){
		
		if(this.moves>0){
			
			let road1=false;
			let road2=false;
			
			for(let a of road){
				
				if(this.x==a.x&&this.y==a.y){
					
					road1=true;
				}
				
				if(selector.x==a.x&&selector.y==a.y){
					
					road2=true;
				}
				
				if(road1&&road2){
					break;
				}
				
			}
			
			if(!road1||!road2){
				
				this.moves--;
				
			}else{
				
				
				this.moves-=0.5;
				
			}
			
			this.x=selector.x;
			this.y=selector.y;
			moveOn=false;
		
		}
		
	}
	
	build(){
		
		let b=true;
		
		for(let a of city){
			
			if(this.x==a.x&&this.y==a.y){
				
				b=false;
				break;
			}
			
		}
		
		if(b){
			
			
			city[city.length]=new City(this.x/size,this.y/size);
			menuCharacter=false;
			
			
		}
		
		
		
	}
	
	road(){
		
		road[road.length]=new Road(this.x,this.y);
		console.log("road");
		
	}
	
}
character=[];

character[0]=new Character(4,3);

class Road{
	
	constructor(x,y){
		this.x=x;
		this.y=y;
	}
	
	draw(){
		c.fillStyle="brown";
		c.fillRect(this.x,this.y+size/3,size,size/3);
		c.fillRect(this.x+size/3,this.y,size/3,size);
	}
	
}

const road=[];

draw();

class Controls{
	
	constructor(){
		this.comprobante=true;
		this.resourceLimit={
			up:6*size,
			down:10*size,
			left:9*size,
			right:13*size
		}
	}
	
	//menuCharacter
	uno(key){
		
		switch(key){
			
			case 'ArrowUp':if(character[currentChar].selector>0){
				character[currentChar].selector-=1;
				}
			break;
			
			case 'ArrowDown':if(character[currentChar].selector<character[0].wordList.length-1){
				character[currentChar].selector+=1;
				}
			break;
			
			case 'x':
			
			switch(character[currentChar].selector){
				
				case 0:moveOn=true; menuCharacter=false; 
				
				character[currentChar].selector=0;
				
				break;
			
				case 1:if(controls.build()){
				
					character[currentChar].build();
					character[currentChar].selector=0;
				}
				
				break;
				
				case 2:character[currentChar].road();
				
				break;
			
			}
			break;
		}
			
		
		this.comprobante=false;
	}
	
	//normal
	dos(key){
		
		switch(key){
					
			case 'ArrowUp':
	 
			if(selector.y>size*2){
		 
		 selector.y-=size;
		
	 }		
	 	 
			break;		
	 
			case 'ArrowRight':
			 
			if(selector.x<canvas.width-size*3){
			 selector.x+=size;
			  }
			  
			 break;	
			 
			 case 'ArrowLeft':
			 
			 if(selector.x>size*2){
			 selector.x-=size;
			 }
			 
			 break;	
			 
			 case 'ArrowDown': 
			 
			 
			 if(selector.y<canvas.height-size*3){
				 selector.y+=size;
			 }
			 break;	
				
			 case 'x':selector.select();
			 break;
			 }
			 
			 this.comprobante=false;
	}
	
	//moveOn
	tres(key){
		
		switch(key){
		
		 case 'ArrowUp':
	 
	     if(selector.y>=character[currentChar].y&&selector.y>size*2){
		 
		       selector.y-=size;
		
	        }		
	 	 
	     break;		
	 
	     case 'ArrowRight':
	 
	      if(selector.x<=character[currentChar].x&&selector.x<canvas.width-size*3){
	          selector.x+=size;
	        }
	  
	       break;	
	 
	       case 'ArrowLeft':
	 
	      if(selector.x>=character[currentChar].x&&selector.x>size*2){
	           selector.x-=size;
	        }
	 
	      break;	
	 
	       case 'ArrowDown': 
	 
	 
	       if(selector.y<=character[currentChar].y&&selector.y<canvas.height-size*3){
		     selector.y+=size;
	        }
	      break;	
		  
		  case 'x':  
		  
		  if(character[currentChar].x!=selector.x||character[0].y!=selector.y){
			  
			  character[currentChar].move();
			  
			  moveOn=false;
			  
		  }
		  
		  break;
	 	
		}
		this.comprobante=false;
	}
	
	//selectUnit
	cuatro(key){
		
		switch(key){
			
			case 'ArrowUp':  
				if(selector.menuSelector>0){
				
					selector.menuSelector-=1
				}
			
			break;
			case 'ArrowDown': 
			
				if(selector.menuSelector<elementos.length-1){
					selector.menuSelector+=1	
				}
				
			break;
			
			case 'x':
			
				if(characters.length>0&&selector.menuSelector<characters.length){
					
					
					character[characters[selector.menuSelector]].menu();
					currentChar=characters[selector.menuSelector];
					selectUnit=false;
					console.log(selector.menuSelector-characters.length);
					
				}
				
				if(selector.menuSelector>=characters.length){
					
					city[cities[selector.menuSelector-characters.length]].menu();
					currentCity=cities[selector.menuSelector-characters.length];
					selectUnit=false;
					cityMenu=true;
				}
				
				
			break;
			
		}
		this.comprobante=false;
	}
	
	//menu de ciudad
	cinco(key){
		
		switch(key){
			
			case 'ArrowUp':
				if(city[currentCity].selector>0){
					city[currentCity].selector--;
				}
			
			break;
			case 'ArrowDown':
		
			if(city[currentCity].selector<city[currentCity].options.length-1){
				city[currentCity].selector++;
			}
			
			break;
			
			case 'x':
			
			if(city[currentCity].selector==0){
				
				cityResources=true;
				cityMenu=false;
				
				selectorAux.x=selector.x;
				selectorAux.y=selector.y;
				selector.x=270;
				selector.y=210;
				
			}

			if(city[currentCity].selector==1){
				productionMenu=true;
				cityMenu=false;
			}

		}
		
	
		
		this.comprobante=false;
	}
	
	//city resource
	seis(key){

		switch(key){
					
			case 'ArrowUp':
	 
				if(selector.y>this.resourceLimit.up){
					
					if(selector.y!=this.resourceLimit.up+size||selector.x!=this.resourceLimit.right){

						if(selector.y!=this.resourceLimit.up+size||selector.x!=this.resourceLimit.left){

							selector.y-=size;

						}
					}
			
				}		
	 	 
			break;		
	 
			case 'ArrowRight':
			 
				if(selector.x<this.resourceLimit.right){
				
				    if(selector.y!=this.resourceLimit.up||selector.x!=this.resourceLimit.right-size){

						if(selector.y!=this.resourceLimit.down||selector.x!=this.resourceLimit.right-size){
	
							
							selector.x+=size;
	
						}
					}
				
				
				}
			  
			break;	
			 
			case 'ArrowLeft':
			 
				if(selector.x>this.resourceLimit.left){

					if(selector.y!=this.resourceLimit.up||selector.x!=this.resourceLimit.left+size){

						if(selector.y!=this.resourceLimit.down||selector.x!=this.resourceLimit.left+size){
	
							
							selector.x-=size;
	
						}
					}

				}
			 
			break;	
			 
			case 'ArrowDown': 
			 
				 if(selector.y<this.resourceLimit.down){

					if(selector.y!=this.resourceLimit.down-size||selector.x!=this.resourceLimit.right){

						if(selector.y!=this.resourceLimit.down-size||selector.x!=this.resourceLimit.left){

						
							selector.y+=size;

						}
					}

				 }
			break;	
				
			case 'x':

				let a=city[currentCity].area[selector.x/size-9][selector.y/size-6];
				
				if(a==true){
					a=false
				}else{
					a=true;
				}

				city[currentCity].area[selector.x/size-9][selector.y/size-6]=a;

				

			break;
			}
		
		this.comprobante=true;
	}

	//seleccionar produccion
	siete(key){
		switch(key){

			case 'ArrowUp':
				if(city[currentCity].productionSelector>0){

					city[currentCity].productionSelector--;
				}

			break;

			case 'ArrowDown':

				if(city[currentCity].productionSelector>city[currentCity].productionSelector.length-1){

					city[currentCity].productionSelector++;
					console.log('se ejecuto');
				}

			break;
		}
	}
	
	//impide construir ciudades cerca de otras
	build(){
		var a=true;
		for(let i=0;i<city.length;i++){
			
			if(character[currentChar].x==city[i].x&&character[currentChar].y==city[i].y){
				
				a=false;
				break;
			}
		}
		return a;
	}	
}

const controls=new Controls;

addEventListener('keydown',({key})=>{
	
		console.log(key);
	
		controls.comprobante=true;
	
		if(menuCharacter&&controls.comprobante){
		
			controls.uno(key);
		}
	
		if(comparar()&&controls.comprobante){
	
			controls.dos(key);
		}
		
		if(selectUnit&&controls.comprobante){
			
			controls.cuatro(key);
		}
		
		if(moveOn&&controls.comprobante){
		
			controls.tres(key);
		}
		
		if(cityMenu&&controls.comprobante){
			
			controls.cinco(key);	
		}
		
		if(cityResources&&controls.comprobante){
			
			controls.seis(key);	
		}
		if(productionMenu&&controls.comprobante){
			controls.siete(key);
		}
		
		
		
		switch(key){
		
			case 'z':menuCharacter=false; 
		        if(moveOn){
					
		          moveOn=false;
				  selector.back();
				}
					cityMenu=false;
					selectUnit=false;
					
				if(cityResources){
					cityResources=false;
					
					cityMenu=true;
					selector.x=selectorAux.x;
					selector.y=selectorAux.y;
					
				}
				if(productionMenu){
					productionMenu=false;
					cityMenu=true;
				}
			break;
	    }
	
		draw();
	});	 