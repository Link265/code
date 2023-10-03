#include <stdio.h>
#include <math.h>
int main(){
    
    printf("ingrese el cateto 1 y el cateto 2: ");

    float cateto1;
    float cateto2;

    scanf("%f %f",&cateto1,&cateto2);
    getchar();

    float hipotenusa = sqrt(pow(cateto1,2) + pow(cateto2,2));

    printf("la hipotenusa es igual a %.2f",hipotenusa);

    return 0;
}