#include<stdio.h>

void linea_mas_larga(FILE * arch,int *mayor,int *num_linea_max);

void linea_mas_larga(FILE * arch,int *mayor,int *num_linea_max){
    *num_linea_max = 1;
    int num_linea_act = 1;
    char letra = 0;
    *mayor = 0;
    int actual = 0;
    while(!feof(arch)){
        if(fscanf(arch,"%c",&letra) == EOF || letra == '\n'){
            if(actual > *mayor){
                *mayor = actual;
                *num_linea_max = num_linea_act;
            }
            actual = 0;
            num_linea_act++;
        }else{
            actual++;
        }   
    }
    if(letra == 0){
        printf("el archivo esta vacio\n");
        *num_linea_max = -1;
        *mayor = -1; 
    }
}

int main(){

    FILE * arch = fopen("entrada_2.txt","r");
    FILE * sal = fopen("salida_2.txt","w");
    int linea;
    int letras;
    if(arch == NULL){
        printf("error abriendo archivo");
        return 1;
    }
    
    linea_mas_larga(arch,&letras,&linea);
    fprintf(sal,"%d %d",letras,linea);

    fclose(arch);
    fclose(sal);
    
    return 0;
}