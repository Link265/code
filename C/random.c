#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100
#define MIN 10

int main(){

    srand(time(NULL));
    printf("el numero random es: %d",rand() % (MAX - MIN) + MIN);    

    return 0;
}