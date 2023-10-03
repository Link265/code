#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <C:\Users\Fabian Tovar\Documents\code\C\tablero.c>
#include <C:\Users\Fabian Tovar\Documents\code\C\movimientos_ajedrez.c>
#include <C:\Users\Fabian Tovar\Documents\code\C\input.c>

int turno = 1;

void draw(){

    printf(" ");

    for(char i = 'A'; i <= 'H' ; i++){
        printf(" %c",i);
    }
    
    for(int i = 0;i < 10;i++){
        if((i > 0) && (i < 9)) printf("%d",9-i);;

        if(i == 9) printf(" ");
        for(int j = 0;j < 10;j++){
            
            if((j == 0) && (i != 0) && (i != 9)){
                printf("|");
            }else if((i > 0 && i < 9) && (j > 0 && j < 9)){
                if(piezas[i-1][j-1][1] == '0')  printf("\033[33m");
                if(piezas[i-1][j-1][1] == '1')  printf("\033[34m");
                printf("%c",piezas[i-1][j-1][0]);

                printf("\033[0m");
                printf("|");
            }   
        }
        printf("\n");
    }
}

void movimiento_enemigo(){
    char tableros[1000][size][size][2];

    for(int i = 0; i < 1000; i++){
        for(int j = 0 ; j < size ; j++){
            for(int h = 0;h < size; h++){
                for(int k = 0; k < 2; k++){
                    tableros[i][j][h][k] = piezas[j][h][k];
                }
            }
        }
    }




}

int main(){
    while (1){
        draw();
        input();
        draw();
        Sleep(1);
        movimiento_enemigo(); 
        turno++;  
    }
    return 0;
}