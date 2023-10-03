#include <stdio.h>

int main(){
    int a;
    scanf("%d");
    char c;
    while(((c = getchar()) != '\n') && c != EOF);//limpiando bufer de entrada
    return 0;
}