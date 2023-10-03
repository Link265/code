const controls = {
	ArrowDown: ()=>{ if(snake.direction != "u"){snake.direction = "d"}},
	ArrowUp: ()=>{ if(snake.direction != "d"){snake.direction = "u"}},
	ArrowLeft: ()=>{ if(snake.direction != "r"){snake.direction = "l"}},
	ArrowRight: ()=>{ if(snake.direction != "l"){snake.direction = "r"}}
}
addEventListener('keydown',({key})=>{
	controls[key]();
});
