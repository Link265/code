#include <stdio.h>

int main(){
    float resultado = 0;
    for(float i =1;i<200;i++){
        resultado+=(i+1)/i;
    }

    printf("%f",resultado);

    return 0;
}