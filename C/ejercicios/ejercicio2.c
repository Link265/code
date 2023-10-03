#include <stdio.h>

int main(){

    printf("ingrese 3 numeros enteros");
    int entero1,entero2,entero3;
    scanf("%d %d %d",&entero1,&entero2,&entero3);

    if(entero1>entero2 && entero1>entero3){
        printf("el %d es mayor que los demas",entero1);
        
    }else if(entero2>entero1 && entero2>entero3){
        printf("el %d es mayor que los demas",entero2);

    }else if(entero3>entero2 && entero3>entero1){
        printf("el %d es mayor que los demas",entero3);

    }    
    return 0;
} 