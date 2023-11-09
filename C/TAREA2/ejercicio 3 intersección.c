#include<stdio.h>

int contar_lineas(FILE * arch);
void copiar_linea(FILE *entrada,FILE *salida);

int contar_lineas(FILE * arch){
    int lineas = 1;
    char letra = 0;
    while(fscanf(arch,"%c",&letra) != EOF){

        if(letra == '\n')   lineas++;
    }
    rewind(arch);
    
    if(letra == 0) return 0;
    
    return lineas;
}

void copiar_linea(FILE *entrada,FILE *salida){
    char letra;
    while(1){
        if(fscanf(entrada,"%c",&letra) == EOF){
            fprintf(salida,"\n");
            break;
        }
            
        fprintf(salida,"%c",letra);
        
        if(letra == '\n')
            break;
    }
}

int main(){
    
    FILE * arch1 = fopen("archivo3_1.txt","r");
    FILE * arch2 = fopen("archivo3_2.txt","r");
    FILE * salida = fopen("salida3.txt","w");
    int lineas;
    
    if(arch1 == NULL || arch2 == NULL || salida == NULL){
        printf("error abriendo archivos");
        return 1;
    }
    
    int lineas_arch1 = contar_lineas(arch1);
    int lineas_arch2 = contar_lineas(arch2);
    
    lineas = (lineas_arch1 < lineas_arch2) ? lineas_arch1 : lineas_arch2;
    
    if(lineas == 0){
        fclose(arch1);
        fclose(arch2);
        fclose(salida);
        printf("uno de los archivos esta vacio");
        return 1;
    }
    
    for(int i = 0; i < lineas; i++){
        copiar_linea(arch1,salida);
        copiar_linea(arch2,salida);
    }
    
    fclose(arch1);
    fclose(arch2);
    fclose(salida);

    printf("intercepcion de archivos creada con exito");
    
    return 0;
}