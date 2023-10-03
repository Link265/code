#include <stdio.h>

int main(){

    int palabras = 0;
    int espacio = 1;

    int c;
    while (((c = getchar()) != EOF) && c != '-'){

        if(((c == ' ') || (c == '\n') || (c == '\t'))){
            espacio = 1;
        }else if(!((c == ' ') || (c == '\n') || (c == '\t')) && espacio){
            palabras++;
            espacio = 0;
        }
    }
    printf("palabras: %d",palabras);
    

    return 0;
}