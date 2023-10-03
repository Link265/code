#include <stdio.h>

int main(){

    printf("L\tM\tM\tJ\tV\tS\tD\t \n");

    printf(" \t \t");
    int j = 0;
    for(int i = 1; i<=31 ;i++){

        
        if(i==6 || j == 7){
            printf("\n");
            j=0;
        }
        printf("%d\t",i);


        j++;
    }

    return 0;
}