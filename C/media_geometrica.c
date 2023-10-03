#include <stdio.h>
#include <math.h>
//calcular media geometrica
int main(){

    int a,b,c;

    printf("ingrese 3 numeros: ");
    scanf("%d %d %d",&a,&b,&c);

    float media_geometrica = cbrt(a*b*c); 

    printf("la media geometrica es %f",media_geometrica);

    return 0;
}