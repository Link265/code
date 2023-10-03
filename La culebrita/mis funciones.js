const d = (x,y,color)=>{
	c.fillStyle = color;
	c.fillRect(x,y,size*0.8,size*0.8);	
};
const reset = ()=>{
	snake.life = true;
	snake.head = 0;
	snake.x = size *5;
	snake.y = size *5;
	snake.tail = [{x:snake.x,y:snake.y}];
	snake.direction = "r";
};