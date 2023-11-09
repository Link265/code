#include<stdio.h>

int contar_palabras(FILE * arch);

int contar_palabras(FILE * arch) {
    char letra;
    int espacio = 1;
    int palabras = 0;
    while(fscanf(arch,"%c",&letra) != EOF) {
        if(letra != ' ' && letra != '\n' && letra != '\t') {
          if(espacio){
            espacio = 0;
            palabras++;
          }
        } else {
            espacio = 1;
        }
    }
    return palabras;
}

int main() {

    FILE * arch = fopen("entrada_1.txt","r");
    FILE * sal = fopen("salida_1","w");
    if(arch == NULL || sal == NULL) {
        printf("error abriendo archivos");
        return 1;
    }

    fprintf(sal,"%d",contar_palabras(arch));

    fclose(arch);
    fclose(sal);
    return 0;
}