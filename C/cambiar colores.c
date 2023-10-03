#include <stdio.h>

int main(){

    //negro
    printf("\033[30m");
    printf("texto negro \n");

    //rojo
    printf("\033[31m");
    printf("texto rojo \n");

    //verde
    printf("\033[32m");
    printf("texto verde \n");

    //amarillo
    printf("\033[33m");
    printf("texto amarillo \n");

    //azul
    printf("\033[34m");
    printf("texto azul \n");

    //magenta
    printf("\033[35m");
    printf("texto magenta \n");

    //cyan
    printf("\033[36m");
    printf("texto cyan \n");

    //blanco
    printf("\033[37m");
    printf("texto blanco \n");

    //por defecto
    printf("\033[0m");
    printf("texto por defecto \n");

    return 0;
}