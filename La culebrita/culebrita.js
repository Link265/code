const field = {
	draw:function (){

		c.fillStyle = "black";
		c.fillRect(0,0,width,height)
	}
}
// const gameOver = {
// 	draw:()=>{
// 		let font = 30;
// 		c.fillStyle = "green";
// 		c.font = font + "px Times New Roman";
// 		c.fillText("Game Over",width/2 - font*2.5,height/2);

// 		font = 20;
// 		c.fillStyle = "green";
// 		c.font = font + "px Times New Roman";
// 		c.fillText("Continue ",width/2 - font*2,height/2 + font *2);
// 	}
// }

class Snake{
	constructor(x,y){
		this.x=x;
		this.y=y;
		this.color = "white";
		this.life = true;
		this.tail = [{x:this.x,y:this.y}];
		this.head = this.tail.length - 1;
		this.direction = "r";
		this.moveTo = {
			l:()=> this.tail[this.head].x -= size,
			r:()=> this.tail[this.head].x += size,
			u:()=> this.tail[this.head].y -= size,
			d:()=> this.tail[this.head].y += size
		};
	}
	move(){
		this.limitMoves();

		for(let i = 0;i < this.head && this.tail.length > 1;i++){
			this.tail[i].x = this.tail[i+1].x;
			this.tail[i].y = this.tail[i+1].y;
		}

		this.moveTo[this.direction]();
	}
	limitMoves(){
		let tail = this.tail[this.head];

		if(tail.x < 0){
			// this.tail[this.head].x = width - size;
			this.life = false;

		}else if(tail.x >= width){
			// this.tail[this.head].x = 0;
			this.life = false;

		}else if(tail.y < 0){
			// this.tail[this.head].y = height - size;
			this.life = false;

		}else if(tail.y >= height){
			// this.tail[this.head].y = 0;
			this.life = false;
		}
		for(let i = 0 ;i < this.tail.length ;i++){

			for(let j = 0; j < this.tail.length;j++){
				if(i == j){
					break;
				}
				if(this.tail[i].x == this.tail[j].x && this.tail[i].y == this.tail[j].y){
					this.life = false;
				}
			}
		}
	}
	draw(){
		for (let i = 0; i < this.tail.length; i++) {
			d(this.tail[i].x,this.tail[i].y,this.color);
		}

	}
	eat(){
		let x = this.tail[this.head].x;
		let y = this.tail[this.head].y;
		if(this.tail[this.head].x == apple.x && this.tail[this.head].y == apple.y){

			switch(this.direction){
				case 'r': x += size;
				break;
				case 'l': x -= size;
				break;
				case 'd': y += size;
				break;
				case 'u': y -= size;
				break;
			}

			this.tail.push({x:x,y:y});

			this.head++;
			apple = new Apple();
		}
	}
}
class Apple{
	constructor(){
		this.color = "red";
		this.colision = true;
		while(true){
			this.x = Math.floor(Math.random() * (width/size-2))*size +size;
			this.y = Math.floor(Math.random() * (height/size-2))*size +size;
			if(this.x != snake.x || this.y != snake.y){
				break;
			}
		}
	}
	draw(){
		d(this.x,this.y,this.color);
	}
}

const snake = new Snake(size*5,size*5);

let apple = new Apple();

const draw = ()=>{
	c.clearRect(0,0,width,height);
	if(snake.life == true && pause != true){

		field.draw();
		snake.draw();
		apple.draw();
	}
	if(snake.life == false){
		reset();
	}
	//score
		let font = 30;
		c.fillStyle = "green";
		c.font = font + "px Times New Roman";
		c.fillText("Score:"+snake.head,width - 150,20);
}
const update = ()=>{
	if(snake.life == true && pause != true){
		snake.move();
		snake.eat();
	}
}

const loop = ()=>{
	update();
	draw();
}
draw();

setInterval(loop,fps);
