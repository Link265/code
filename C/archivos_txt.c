#include <stdio.h>
#include <stdlib.h>


int main(){

    FILE *archivo;

    char nombreArchivo[100];
    char contenido[100];

    printf("Ingrese el nombre del archivo que desea modificar: ");
    scanf("%s", nombreArchivo);

    archivo = fopen(nombreArchivo, "a");

    if (archivo == NULL) {
        printf("No se pudo abrir el archivo. Verifique que el nombre sea correcto y que tenga permisos de escritura.\n");
        return 1;
    }

    printf("Ingrese el nuevo contenido del archivo: ");
    scanf(" %[^\n]", contenido);

    fprintf(archivo, "%s", contenido);

    fclose(archivo);

    printf("El archivo ha sido modificado exitosamente.\n");

    return 0;
}