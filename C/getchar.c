//getchar y putchar
#include <stdio.h>

//getchar puede ser usado para limpiar el bufer de entrada
// y consume menos recursos que print

int main(){

    int x = getchar();
    while(x != EOF){
        putchar(x);
        x = getchar();
    }

    return 0;
}