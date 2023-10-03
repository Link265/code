#include <stdio.h>

struct persona{
    char nombre[20];
    int edad;
    char profesion[20];
};


int main(){

    struct persona p1 = {"Link",14,"heroe"};

    printf("nombre: %s \n",p1.nombre);
    printf("edad: %d \n",p1.edad);
    printf("profesion: %s \n",p1.profesion);

    return 0;
}