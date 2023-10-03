#include <stdio.h>

int main(){
    printf("ingrese un numero entero: ");
    int a;
    scanf("%d",&a);
    printf("%d \n",a);

    //limpiando el bufer de entrada con getchar()
    getchar();


    // gets(a) es otro metodo que no se de detiene cuando ve un espacio a diferencia de scanf
    char b[30];
    printf("ingrese una cadena: ");
    gets(b);
    printf("%s",b);


    return 0;
}