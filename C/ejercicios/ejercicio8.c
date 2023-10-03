#include <stdio.h>

int main(){

    printf("ingrese cuantas lineas quiere: ");
    int n;
    scanf("%d",&n);

    for (int i = 1; i <= n; i++){
        for (int j = 0; j < i; j++){
            printf("*");
        }
        printf("\n");
    }
    

    return 0;
}