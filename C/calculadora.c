#include <stdio.h>

float sumar(float a,float b){
    return (a + b);
}
float multiplicar(float a,float b){
    return (a*b);
}
float restar(float a,float b){
    return (a-b);
}
float dividir(float a,float b){

    if(b == 0){
        puts("la division es invalida");
        return 0;
    }

    return (a/b);
}


int main(){

    //preguntando al usuario
    puts("que operacion desea realizar?");
    puts("1.sumar");
    puts("2.restar");
    puts("3.multiplicar");
    puts("4.dividir");

    //leyendo entrada del usuario
    int eleccion;
    scanf("%d",&eleccion);

    //leyendo los numeros
    printf("ingrese los numeros: ");
    float x;
    float y;
    scanf("%f %f",&x,&y);

    //estableciendo los casos
    float resultado;
    switch (eleccion){
        case 1:resultado = sumar(x,y);
            break;
        case 2:resultado = restar(x,y);
            break;
        case 3:resultado = multiplicar(x,y);
            break;    
        case 4:resultado = dividir(x,y);
            break;
        default:printf("por favor ingrese una entrada valida");
            break;
    }

    //mostrando el resultado
    printf("el resultado es igual a: %.1f",resultado);

    return 0;
}