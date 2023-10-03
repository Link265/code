#include <stdio.h>

int main(){
    
    int a = 13;
    int *b = &a;
   
    printf("a = %d \n",a);
    printf("&a = %d \n",&a);
    printf("b = %d \n",b);
    printf("*b = %d \n",*b);

    return 0;
}