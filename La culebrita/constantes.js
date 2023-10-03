const canvas = document.getElementById("canvas");
const c = canvas.getContext("2d");
const size = 30;

const calculateScreenSize = (screenSize) =>{

  while(true){
    if(screenSize % size == 0){
      break;
    }
    screenSize--;
  }
  return screenSize;
}

canvas.width = calculateScreenSize(innerWidth);
canvas.height = calculateScreenSize(innerHeight);
const {width} = canvas;
const {height} = canvas;
const fps = 1000/10;
let pause = false;
