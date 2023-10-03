#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void colorear(int a){
    //1 rojo
    //2 verde
    //3 amarillo
    //4 azul
    printf("\033[3%dm",a);
}
void limpiar(){
    int c;
    while(((c = getchar()) != '\n') && (c != EOF));
} 


int main(){

    FILE *a = fopen("C:\\Users\\Fabian tovar\\Desktop\\file.txt","a");

    fprintf(a,"%s","hola");

    fclose(a);

    return 0;
}

