#include <stdio.h>

float calculadora(numero1,numero2,operacion){

   

    switch(operacion){
        case '+':return (numero1+numero2);
        break;
        case '-':return (numero1-numero2);
        break;
        case '/':return (numero1/numero2);
        break;
        case '*':return (numero1*numero2);
        break; 
        default:return 89;
        break;
    }

}


int main(){

    printf("calculadora version 5.34\n :");
    int a;
    int b;
    char c;

    scanf("%d %c %d",&a,&c,&b);
    printf("%d \n",(c=='+'));

    float resultado = calculadora(a,b,c);  
    
    printf("el resultado es %.2f",resultado);

    return 0;
}