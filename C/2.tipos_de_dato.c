#include <stdio.h>

int main(){
    char a = 'c'; //1 byte
    int b = 10000;//-32.000 ... 32.000 //2 byte
    unsigned int c = 40000;//0 ... 64.000 //2 byte
    float d = 34.55;//
    double f = 54.009;
    long h = 60.000;
    short y = 100;// -256 ... 256
    char cadena[] ="hola";

    /*%c - "char" "unsigned char"
    %d - "int"
     %i - "short" "int" "unsigned int" 
    %li - "long"
     %f - "float"
     %lf - "double"
     %Lf - "long double"
    %s - "char texto[n]" secuencia de caracter*/

    printf("%lf",f);
    
    printf("");
    return 0;
}
