//C orrija la rutina principal del program a de la línea más larga de 
//modo que imprima correctamente la longitud de líneas de entrada arbitrariamente 
//largas, y tanto texto como sea posible

#include<stdio.h>
#include<string.h>

#define limite 1000

void reverse(char arr[limite]){

    char arr_temp[limite];

    copy(arr,arr_temp);

    for(int i = strlen(arr_temp)-1;i >= 0;i--){
        arr[i] = arr_temp[strlen(arr_temp) - i];
    }
    
    

}

void copy(char from[],char to[]){
    int i;
    for(i = 0; i < strlen(from);i++){
        to[i] = from[i];
    }
    to[i] = '\0';
}

int main(){

    
    
    



    return 0;
}
