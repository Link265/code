#include <stdio.h>

int main(){

    int variable = 1;
    int * a;
    a = &variable;

    *a += 1;

    printf("%d",*a);

    return 0;
}