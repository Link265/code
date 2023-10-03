const {createServer} = require('http');
const {createReadStream} = require('fs');
const {port = 3000} = process.env;
const handle = (req,res)=>{
	res.writeHead(200,{'Content-Type':'text/html'});
	createReadStream('/home/fabian/Documents/code/node/HTML 1.html').pipe(res);
	
}

const server = createServer(handle);

server.listen(port,function(){
	console.log(`servidor montado en puerto:${port}`);
});