#include <stdio.h>
#include <stdlib.h>

#define PENDIENTES 1
#define TERMINADAS 0
#define true 1
#define false 0
#define TAREAS_PENDIENTES "lista_de_tareas_pendientes.txt"
#define TAREAS_TERMINADAS "lista_de_tareas_terminadas.txt"

int agregar_tarea(char [100]);
int terminar_tarea(int id_tarea);
void mostrar_menu(void);
int ver_tareas(int tipo);
void limpiar_buffer(void);
int eliminar_linea(FILE * archivo,char nombre_de_archivo[30],int linea);
void recibir_entrada(void);
int inicializar_archivos(void);
int crear_archivo(char nombre_de_archivo[100]);
void borrar_tareas_terminadas(void);

void limpiar_buffer(void){
    while(getchar() != '\n');
}

int eliminar_linea(FILE * archivo,char nombre_de_archivo[30],int numero_de_linea){

    char linea[100];
    FILE * aux = fopen("auxiliar.txt","w");
    if(aux == NULL){
        printf("error borrando la linea\n");
        return false;
    }

    rewind(archivo);

    int i;
    for(i = 1;fgets(linea,100,archivo); i++){
        if(i != numero_de_linea)
            fputs(linea,aux);
    }
    if(i < numero_de_linea){
        remove("auxiliar.txt");
        printf("linea no encontrada\n");
        return false;
    }
    fclose(archivo);
    fclose(aux);

    if(!remove(nombre_de_archivo) || !rename("auxiliar.txt",nombre_de_archivo)){
        return false;
    }

    archivo = fopen(nombre_de_archivo,"r");

    return true; // retorna 1 si la operacion fue exitosa
}

int agregar_tarea(char tarea[100]){
    FILE * arch = fopen("lista_de_tareas_pendientes.txt","a");

    if(arch == NULL){
        printf("no se pudo abrir el archivo\n");
        return false;
    }    

    fprintf(arch,"%s\n",tarea);
    fclose(arch);

    return true; // retorna true si la operacion fue exitosa
}

void mostrar_menu(void){

    printf("1) Ver tareas pendientes\n");
    printf("2) Ver tareas terminadas\n");
    printf("3) Agregar nueva tarea\n");
    printf("4) Agregar tarea a la lista de terminadas\n");
    printf("5) borrar la lista de terminadas\n");
    printf("Eleccion: ");
}

int ver_tareas(int tipo){

    FILE * arch;
    char tarea[30];
    int num = 0;

    if(tipo == TERMINADAS){
        arch = fopen("lista_de_tareas_terminadas.txt","r");
    }else if(tipo == PENDIENTES){
        arch = fopen("lista_de_tareas_pendientes.txt","r");
    }else{
        printf("ERROR INTERNO\n");
        return false;
    }

    if(arch == NULL){
        printf("Error abriendo archivo de guardado\n");
        return false;
    }

    printf("\nLista:\n");
    while (fscanf(arch,"%[^\n]%*c",tarea) != EOF){
        num++;
        printf("%d) %s\n",num,tarea);
    }
    if(num == 0){
        printf("(VACIO)\n");
    }
    printf("\n");

    fclose(arch);
    return true; // retorna true si la operacion fue exitosa
}

void recibir_entrada(void){

    char entrada;
    char tarea[30];
    int id_tarea;
    int validacion_del_scanf;

    entrada = getchar();
    limpiar_buffer();

    switch (entrada){
    case '1':
        ver_tareas(PENDIENTES);
        break;
    case '2':
        ver_tareas(TERMINADAS);
        break;
    case '3':
        printf("ingrese la tarea que va a agregar: ");
        scanf("%s",tarea);
        limpiar_buffer();
        agregar_tarea(tarea);
        break;
    case '4':
        ver_tareas(PENDIENTES);

        while (true){
            
            printf("Ingrese el numero de la tarea que desea marcar como terminada: ");
        
            validacion_del_scanf = scanf("%d",&id_tarea);
            limpiar_buffer();
            
            if(validacion_del_scanf != 1){
                printf("entrada invalida\n");
                continue;
            }
            break; 
        }
        if(terminar_tarea(id_tarea)){
            printf("operacion realizada con exito\n");
        }
        break;
    case '5':
        borrar_tareas_terminadas();
        break;    
    default:
        printf("ingreso una entrada erronea intente otra vez\n");
        break;
    }
}

int terminar_tarea(int id_tarea){

    FILE * tareas_pendientes = fopen("lista_de_tareas_pendientes.txt","r");
    FILE * tareas_terminadas = fopen("lista_de_tareas_terminadas.txt","a");

    char cadena[100];
    int validador;

    if(tareas_pendientes == NULL || tareas_terminadas == NULL){
        printf("error con archivos de guardado\n");
        return false;
    }

    for(int i = 0; i < id_tarea; i++){
        if(fscanf(tareas_pendientes,"%[^\n]%*c",cadena) == EOF){
            printf("el numero insertado excede el numero de tareas que hay\n");
            fclose(tareas_pendientes);
            fclose(tareas_terminadas);
            return false;
        }
    }
    fprintf(tareas_terminadas,"%s\n",cadena);

    validador = eliminar_linea(tareas_pendientes,"lista_de_tareas_pendientes.txt",id_tarea);

    fclose(tareas_pendientes);
    fclose(tareas_terminadas);

    if(!validador){
        return false;
    }
    return true; // retorna true si la operacion fue exitosa
}

int crear_archivo(char nombre_de_archivo[100]){
    if(fopen(nombre_de_archivo,"r") == NULL){
        if(fopen(nombre_de_archivo,"w") == NULL){
            return false;
        }
    }
    return true;
}

int inicializar_archivos(void){
    if(crear_archivo(TAREAS_PENDIENTES) && crear_archivo(TAREAS_TERMINADAS)){
        return true;
    }
    return false;
}

void borrar_tareas_terminadas(void){
    FILE * arch = fopen(TAREAS_TERMINADAS,"w");
    fprintf(arch,"");
}

int main(){

    if(!inicializar_archivos()){
        printf("no se pudo crear los archivos de guardado");
        return 1;
    }
    printf("###bienvenido al gestor de tareas###\n\n");

    while(true){
        mostrar_menu();
        recibir_entrada();
    }
    return 0;
}