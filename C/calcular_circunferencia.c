#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
int main(){

    printf("ingrese el radio de la circunferencia: ");
    float radio;
    scanf("%f",&radio);

    float circunferencia = 2 * M_PI * radio;

    printf("la circunferencia es igual a: %f",circunferencia);

    return 0;
}