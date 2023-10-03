#include <stdio.h>
#include <math.h>

int longitud(int num){
    int lenght = 0;
    while(num > 0){
        lenght++;
        num=num/10;
    }
    return lenght;
}

int decimal_to_binary(int num){
    int resul = 0;
    int n = 0;
    int i = 0;
    while(n<num){
        n = pow(2,i);
        i++;
    }
    n = pow(2,i-1);


    

    return resul;
}



int binary_to_decimal(int num){
    int lenght = longitud(num);
    int resul = 0;
    for(int i = 0;i < lenght; i++){
        int digit = num%10;
        resul += (digit * pow(2,i));
        num /=10;
    }
    return resul;
}


int main(){
    printf("%d \n",binary_to_decimal(110));
    return 0;
}