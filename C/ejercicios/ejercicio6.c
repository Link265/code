#include <stdio.h>

int main(){

    printf("cuantas notas desea ingresar? : ");
    int numero_de_notas;
    scanf("%d",&numero_de_notas);

    int notas[numero_de_notas];

    for(int i = 0;i < numero_de_notas;i++){
        printf("ingrese la nota numero %d: ",i);
        scanf("%d",&notas[i]);
    }

    int suma_de_notas = 0;
    for(int i = 0;i < numero_de_notas;i++ ){
        suma_de_notas+=notas[i];
    }

    int promedio = suma_de_notas/numero_de_notas;    
    printf("el promedio es igual a: %d",promedio);



    return 0;
}