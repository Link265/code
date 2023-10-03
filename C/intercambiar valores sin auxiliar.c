#include <stdio.h>
int main(){

    int a;
    int b;
    
    printf("ingrese 2 numeros: ");
    scanf("%d %d",&a,&b);

    int c;
    while(((c = getchar()) != '\n') && c != EOF);

    printf("el valor de a es: %d \n",a);
    printf("el valor de b es: %d \n",b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("el nuevo valor de a es: %d \n",a);
    printf("el nuevo valor de b es: %d \n",b);

    return 0;
}    