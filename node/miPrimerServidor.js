//mi primer servidor
const http = require("http");
const port=8000;
const handle=function(req,res){
	//codigo 200 means todo va bien
	res.writeHead(200,{"Content-Type":"text/html"});
	res.write("Hola");
	res.end();
}

const server = http.createServer(handle)

//listen() elige el puerto del servidor
server.listen(port,function(){
	console.log(`servidor montado en puerto:${port}`);
});