#include <stdio.h>
#include <string.h>

int main(){
    

    char a[5] = "hola";
    char b[] = "holaaa";

    // la funcion strcmp retorna 0 si las cadenas son iguales 
    // retorna -1 si la primera cadena es prioridad alfabeticamente
    // retorna 1 si la primera cadena va despues alfabeticamente
    printf("%d \n",strcmp(a,b));
    
    //la funcion strlen retorna la longitud de la cadena
    printf("%d \n",strlen(a));

    return 0;
}