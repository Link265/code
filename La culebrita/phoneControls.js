const U = document.querySelector(".U");
const D = document.querySelector(".D");
const L = document.querySelector(".L");
const R = document.querySelector(".R");

U.addEventListener('click',()=>{
  snake.direction = "u";
});
D.addEventListener('click',()=>{
  snake.direction = "d";
});
R.addEventListener('click',()=>{
  snake.direction = "r";
});
L.addEventListener('click',()=>{
  snake.direction = "l";
});
