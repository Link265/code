#include <stdio.h>



int main(){

    int a,b,c;
    printf("inserte 3 numeros: ");
    scanf("%d %d %d",&a,&b,&c);

    float media = (a + b + c)/3;

    printf("la media es: %.2f",media);

    return 0;
}