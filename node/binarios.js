const binary = (num) =>{
	let cadena = "";
	let result;
	for (let i = 128 ; i > 0.5; i/=2) {
		if(num >= i){
			cadena += "1";
			num -= i;
		}else{
			cadena += "0";
		}
	}
	return cadena;
}
let a = 2;
let b = 5;

console.log("a="+a+"="+binary(a));
console.log("b="+b+"="+binary(b));

console.log("a = "+a+" ^ "+b);
a^=b;
console.log("nuevo a = "+a+"="+binary(a));
console.log("b = "+a+" ^ "+b);
b^=a;
console.log("nuevo b = "+b+"="+binary(b));
console.log("a = "+a+" ^ "+b);
a^=b;

console.log("ultimo a = "+a+"="+binary(a));