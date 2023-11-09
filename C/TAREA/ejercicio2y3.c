#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define true 1
#define false 0

void inicializar_datos_de_juego(int *,int *,int *width,int *height,int *x,int *y);
int no_es_una_posicion_segura(int x,int y,int x_origen,int y_origen,int width,int height);
void terremoto(int *,int *);
int elegir_dificultad(void);
void limpiar_buffer(void);

void limpiar_buffer(void){
    while(getchar() != '\n'); 
    // la funcion getchar() limpia los caracteres encontrados 
    //en el bufer de entrada hasta encontrar un salto de linea( \n )     
}

void inicializar_datos_de_juego(int *x_mapa,int *y_mapa,int *width,int *height,int *x,int *y){

    FILE * archivo = fopen("datos_iniciales.txt","r");

    fscanf(archivo ,"%d", x_mapa);
    fscanf(archivo ,"%d", y_mapa);
    fscanf(archivo ,"%d", width);
    fscanf(archivo ,"%d", height);

    fclose(archivo);

    srand(time(NULL));
    *x = rand() % (*width - *x_mapa + 1) + *x_mapa;

    srand(time(NULL));
    *y = rand() % (*height - *y_mapa + 1) + *y_mapa;
}

int no_es_una_posicion_segura(int x,int y,int x_origen,int y_origen,int width,int height){

    if(x_origen <= x && x <= (x_origen + width) && y_origen <= y && y <= (y_origen + height)) 
        return false; // es segura

    return true;// no es segura
}

void terremoto(int *x,int *y){

    const int maximo = 5;
    const int minimo = 1;
    int desplazamiento;
    int direccion;

    srand(time(NULL));
    desplazamiento = rand() % maximo + minimo;

    srand(time(NULL));
    direccion = rand() % (maximo - 1) + minimo;

    switch(direccion){
        case 1:
            *x += desplazamiento;
            break;
        case 2:
            *x -= desplazamiento;
            break;
        case 3:
            *y += desplazamiento;
            break;
        case 4:
            *y -= desplazamiento;     
    }
}

int elegir_dificultad(void){

    int dificultad;
    int tecla;

    while (true){
        
        printf("elija la dificultad:\n");
        printf("1:facil \n2:normal \n3:dificil \n4:macho alfa \nopcion: ");
        scanf("%d",&tecla);
        limpiar_buffer();

        switch (tecla){
        case 1:
            dificultad = 8; //terremoto cada 8 turnos
            break;
        case 2:
            dificultad = 6; //terremoto cada 6 turnos
            break;
        case 3:
            dificultad = 4; //terremoto cada 4 turnos
            break;    
        case 4:
            dificultad = 2; //terremoto cada 2 turnos
            break;

        default:
            printf("entrada incorrecta\n");
            continue;
        }
        break;
    }
    return dificultad;
}

int main(){

    char tecla;
    int vida = 10;
    int turnos = 0;
    int k;//dificultad
    int x,y;//posicion del jugador
    int x_origen,y_origen,ancho,altura;//dimesiones del mapa

    inicializar_datos_de_juego(&x_origen,&y_origen,&ancho,&altura,&x,&y);

    printf("Instrucciones del juego:\n");
    printf("si sales de la zona segura perderas 1 punto de vida por turno\n");
    printf("la zona segura esta entre el punto (%d,%d) y (%d,%d)\n",x_origen,y_origen,x_origen + ancho,y_origen + altura);
    printf("un terremoto movera la zona segura de posicion cada tantos turnos dependiendo de la dificultad\n");

    k = elegir_dificultad();
    
    while(true){

        turnos++;
        printf("\nturno: %d",turnos);
        printf("\tvida: %d",vida);
        printf("\tposicion actual: %d %d\n",x,y);

        printf("teclas de movimiento:  w:arriba  a:izquierda  d:derecha  s:abajo\n");
        printf("eleccion: ");
        scanf("%c",&tecla);
        limpiar_buffer();

        switch (tecla){
            case 'w':
                y -= 1;
                break;
            case 'a':
                x -= 1;
                break;
            case 'd':
                x += 1;
                break;
            case 's':
                y += 1;
                break;
            default:
                printf("entrada no valida\n");
                continue;
        }
        if(turnos % k == 0){
            terremoto(&x_origen,&y_origen);
            printf("\n##HA OCURRIDO UN TERREMOTO##\n");
            printf("Ahora la zona segura esta entre: (%d,%d) y (%d,%d)\n",x_origen,y_origen,x_origen + ancho,y_origen + altura);
        }  
            
        if(no_es_una_posicion_segura(x,y,x_origen,y_origen,ancho,altura)){
            vida--;
            printf("\n##PERDIO UN PUNTO DE VIDA##\n");
        }

        if(vida == 0){
            printf("\nse ha quedado sin vidas\n");
            printf("GAME OVER\n");
            printf("puntuacion: %d\n",turnos);

            printf("quiere volver a intentar? \nS:si \ncualquier otra letra:no \neleccion: ");
            scanf("%c",&tecla);
            limpiar_buffer();
            if(tecla == 'S' || tecla == 's'){
                turnos = 0;
                vida = 10;
                inicializar_datos_de_juego(&x_origen,&y_origen,&ancho,&altura,&x,&y);
                k = elegir_dificultad();

                continue;
            }
            break;
        }    
    }
    return 0;
}