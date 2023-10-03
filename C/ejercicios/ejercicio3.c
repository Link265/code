#include <stdio.h>

int main(){

    printf("ingrese 2 numeros enteros: ");
    int entero1,entero2;
    scanf("%d %d",&entero1,&entero2);

    if(entero2%entero1 == 0){
        printf("%d es multiplo de %d",entero2,entero1);
    }else if(entero1%entero2 == 0){
        printf("%d es multiplo de %d",entero1,entero2);
    }else{
        printf("niguno se multiplo del otro");
    }

    return 0;
} 