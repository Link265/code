#include <stdio.h>

int main(){

    int a = 32000;
    int b[10] = {32,43,54,221,56,67};
    char g[10];


    // para entender como obtener la longitud de de un array
    // primero hay que entender como funciona la funcion sizeof
    printf("%d \n",sizeof(a));
    //en este ejemplo la funcion retorna el espacio acupado por el 
    // entero a
    // esto nos dice que cada entero ocupa 4 bytes de memoria

    //aqui usamos la funcion en un array de enteros
    //retornara el espacio ocupado por el array
    printf("%d \n",sizeof(b));
    //si cuanto ocupa cada entero podemos facilmente deducir
    //cuantos elementos posee

    int longitud = sizeof(b)/sizeof(a);
    //simplemente dividimos el espacio cupado por el 
    // array entre lo que ocupa cada entero

    printf("%d\n",longitud);

    printf("%d",g[9]);

    return 0;
}