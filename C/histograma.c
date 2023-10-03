#include <stdio.h>
#include <stdbool.h>

int main(){

    bool espacio = false;
    int c;
    while (((c = getchar()) != EOF) && (c != '\n')){

        if(((c == ' ') || (c == '\t'))){
            if(!espacio){
                putchar('\n');
                espacio = true;
            }
        }else{
            putchar('|');
            espacio = false;
        }

    }
    return 0;
}