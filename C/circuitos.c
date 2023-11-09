#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#define MAX_SIZE 4

int decimal_to_binary(int);
void copy_to(int from[MAX_SIZE][MAX_SIZE],int to[MAX_SIZE][MAX_SIZE]);

int height,width;
int mapa_de_karnaugh[MAX_SIZE][MAX_SIZE];

void copy_to(int from[MAX_SIZE][MAX_SIZE],int to[MAX_SIZE][MAX_SIZE]){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            to[i][j] = from[i][j];
        }
    }
}

void karnaugh_dimensiones(int numero_de_parametros){
    if(numero_de_parametros == 4){
        width = 4;
        height = 4;
    }else if(numero_de_parametros == 3){
        width = 4;
        height = 2;
    }else{
        width = 2;
        height = 2;
    }
}

void limpiar(void){
    int c;
    while((c = getchar()) != EOF && c != '\n');
}

int decimal_to_binary(int a){
    int binary = 0;
    int potencia;
    for(potencia = 0; pow(2,potencia) < a; potencia++);

    for(int i = potencia; a > 0; i--){
        binary *= 10;
        if(pow(2,i) <= a){
            a -= pow(2,i);
            binary++;
        }
    }
    return binary;
}

void inicializar_mapa_de_karnaugh(){
    int values[] = {0,1,3,2,4,5,7,6,12,13,15,14,8,9,11,10};
    int index = 0;
}

void show_karnaugh(char para[4],int terms[30],int terms_num){
    int values[] = {0,1,3,2,4,5,7,6,12,13,15,14,8,9,11,10};
    int index = 0;
    int width;
    int height;

    if(width == 2){
        values[2] = 2;
        values[3] = 3;
    }
    int karnaugh[height][width];

    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            karnaugh[i][j] = 0;
            for(int k = 0; k < terms_num ; k++){
                if(values[index] == terms[k]){
                    karnaugh[i][j] = 1;
                    break;
                }   
            }
            index++;
        }
    }

    index = 0;
    printf("\nMapa de karnaugh:\n   ");
    for(int i = 0; i < width; i++) printf("   %d",decimal_to_binary(values[index++]));
    printf("\n   ");
    index = 0;
    for(int i = 0 ; i < height ; i++){
        printf("%2d|",decimal_to_binary(values[index++]));
        for(int j = 0; j < width ; j++)
            printf(" %d |",karnaugh[i][j]);
        
        printf("\n   ");
    }
}

void calcular_formula(char parametros[4],int height,int width){
    int values[] = {00,01,11,10};
    int karnaught[height][width];

    int derecha = 0;
    int abajo = 0;

    int posiciones_ya_revisadas_x[16];
    int posiciones_ya_revisadas_y[16];

    for(int i = 0; i < 16;i++){ 
        posiciones_ya_revisadas_x[i] = -1;
        posiciones_ya_revisadas_y[i] = -1;
    }
    
    int index = 0;
    int continuar;
    int square = 0;

    char negacion[100];
    int index_negacion = 0;
    char formula[100];
    int index_formula = 0;

    for(int i = 0; i < height; i++){
        for(int j = 0; j < width ; j++){
            continuar = 0;
            for(int k = 0; k < 16; k ++){
                if(posiciones_ya_revisadas_x[k] == j && posiciones_ya_revisadas_y[k] == i){
                    continuar = 1;
                    break;
                }
            }

            if(continuar) continue;

            if(karnaught[i][j]){
                if(j != width-1 && karnaught[i][j+1]){
                    derecha = 1;
                }
                if(i != height-1 && karnaught[i+1][j]){
                    abajo = 1;
                }
                if(derecha && abajo && karnaught[i+1][j+1]){
                    square = 1;
                    posiciones_ya_revisadas_x[index] = j + 1;
                    posiciones_ya_revisadas_y[index] = i + 1;
                    index++;
                }
                posiciones_ya_revisadas_x[index] = j + 1;
                posiciones_ya_revisadas_y[index] = i;
                index++;
                posiciones_ya_revisadas_x[index] = j;
                posiciones_ya_revisadas_y[index] = i + 1;
                index++;

            }

        }
    }
}

int main(){

    char parametros[4];
    int min_terms[15];
    for(int i = 0; i < 15; i++) min_terms[i] = -1;

    int c;
    int parametros_quantity = 0;
    int min_terms_quantity = 0;
    bool space = false;

    printf("ingrese los parametros de la funcion(maximo 4): ");
    while((( (c = getchar()) != '\n') || (parametros_quantity < 2)) && (parametros_quantity < 4) ){
        if(((c >= 'a') && (c <= 'z')) || ((c >= 'A') && (c <= 'Z'))){
            parametros[parametros_quantity] = c;
            parametros_quantity++;
        }
    }
    if(c != '\n'){
        limpiar();
    }
    
    printf("ingrese los min terms(maximo 30): ");
    while (((c = getchar()) != '\n') && (min_terms_quantity < 4) ){//pidiendo minterminos
        if((c == ' ') && space){
            min_terms_quantity++;
            space = false;
            continue;
        }
        if((c <= '9') && (c >= '0')){
            space = true;
            if(min_terms[min_terms_quantity] == -1) min_terms[min_terms_quantity] = 0;

            min_terms[min_terms_quantity] *= 10;
            min_terms[min_terms_quantity] += c - '0';
        }
    }
    min_terms_quantity++; // no se cuenta el ultimo termino durante el bucle
    if(c != '\n'){
        limpiar();
    }
    karnaugh_dimensiones(parametros_quantity);
    int karnaugh_global[height][width];
    show_karnaugh(parametros,min_terms,min_terms_quantity);

    return 0;
}