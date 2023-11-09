#include <stdio.h>

#define MAX 127
#define MIN 33
#define true 1
#define false 0

void limpiar_buffer(void);
int encriptar(FILE * archivo,int llave);
int desencriptar(FILE * archivo,int llave);

void limpiar_buffer(void){
    while(getchar() != '\n');
    // limpia el buffer de entrada hasta que encuentra el fin de linea(\n) 
}

int encriptar(FILE * archivo,int llave){

    FILE * encriptado = fopen("encriptacionFT.txt","w");
    if(archivo == NULL){
        printf("error creando archivo de encriptacion\n");
        return false;
    }
    char caracter; 

    while (fscanf(archivo,"%c",&caracter) != EOF){
        
        if(caracter > MIN - 1){
            if(caracter + llave > MAX)
                caracter += (caracter + llave) % MAX + MIN - 1;
            else
                caracter += llave;
        }

        fprintf(encriptado,"%c",caracter);
    }

    fclose(encriptado);

    return true;
}

int desencriptar(FILE * archivo,int llave){

    FILE * desencriptacion = fopen("desencriptacionFT.txt","w");
    if(desencriptacion == NULL){
        printf("error creando archivo de desencriptado\n");
        return false;    
    }
    char caracter;

    while(fscanf(archivo,"%c",&caracter) != EOF){
        
        if(caracter > MIN - 1){
            if(caracter - llave < MIN)
                caracter += MAX - MIN - 1 - llave;
            else
                caracter -= llave;
        }
        fprintf(desencriptacion,"%c",caracter);
    }

    fclose(desencriptacion);

    return true;
}


int main(){

    FILE * archivo;
    char nombre[100];
    int numero_llave;
    int opcion;
    int validacion_del_scanf;

    while(true){//bucle para validar

        //obteniendo nombre del archivo
        printf("ingrese el nombre del archivo: ");
        scanf("%s",nombre); 
        limpiar_buffer();
        archivo = fopen(nombre,"r");
        if(archivo == NULL){
            printf("archivo no encontrado\n");
            continue;
        }
        break;
    }

    while(true){//bucle para validar
        
        //obteniendo valor llave
        printf("ingrese el valor llave(entre 1 y %d): ",MAX - MIN - 1);
        validacion_del_scanf = scanf("%d",&numero_llave);
        limpiar_buffer();

        if(numero_llave > MAX - MIN - 1 || numero_llave < 1){
            printf("la llave se sale del rango\n");
            continue;
        }

        if(validacion_del_scanf) break;

        printf("ingreso una entrada invalida\n");
    }

    while(true){//bucle para validar
        
        //pidiendole la opcion al usuario
        printf("1: encriptar \n2: desencriptar \neleccion: ");
        scanf("%d",&opcion);
        limpiar_buffer();

        switch(opcion){
            case 1 : 
                printf("encriptando...\n");
                if(encriptar(archivo,numero_llave))
                    printf("se ha encriptado con exito en el archivo encriptacionFT.txt");
                else
                    printf("algo ha salido mal\nporfavor reinicie el programa");

                break;
            case 2 :
                printf("desencriptando...\n");
                    if(desencriptar(archivo,numero_llave))
                        printf("se ha desencriptado con exito en el archivo desencriptacionFT.txt");
                    else
                        printf("algo ha salido mal\nporfavor reinicie el programa");         
                break;

            default:
                printf("opcion invalida\n");
                continue;
        }
        break;
    }
    fclose(archivo);
    return 0;
}