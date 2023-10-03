#include <stdio.h>
#include <math.h>

int max(int array[],int longitud){

    int maximo = 0;

    for(int i = 0; i < longitud; i++)
        if(array[i] > maximo ) maximo = array[i];
    
    return maximo;
}


int main(){

    int letras[100];

    for(int i = 0; i < 100 ; i++){
        letras[i]  = 0;
    }
    int palabra = 0;

    short espacio = 0;

    int c;

    while(((c = getchar()) != EOF) && (c != '\n')){
        if((c != ' ') && (c != '\t')){
            letras[palabra]++;
            espacio = 1;
        }else{
            if(espacio){
                palabra++;
            }
            espacio = 0;
        }
    }
    for(int y = 0; y < max(letras, sizeof(letras)/sizeof(letras[0])) ; y++){
        for(int x = 0; x < 100;x++){

            if(letras[x] >= (max(letras, sizeof(letras)/sizeof(letras[0])) - y))
                printf("= ");
            else
                printf("  ");
            
        }
        printf("\n");
    }

    return 0;
}