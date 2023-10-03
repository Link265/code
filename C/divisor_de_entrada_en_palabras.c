#include <stdio.h>
#include <stdbool.h>

int main(){

    int c;
    while(((c = getchar()) != EOF) && c != '-'){

        if((c != '\n') && (c != ' ') && (c != '\t')){
            putchar(c);
        }else{
            putchar('\n');
        }

    }


    return 0;
}