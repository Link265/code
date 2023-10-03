#include <stdio.h>

//macros
#define a 512

int square(int x){
    int s = x*x;

    return s; 
}



int main(){

    printf("hellow new world %i \n",a);
    int b = square(2);
    printf("%i",b);
    return 0;
}