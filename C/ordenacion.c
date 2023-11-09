#include <stdio.h> 

int shellsort(int arr[],int length){

    int count = 0;

    for(int gap = length/2;gap > 0 ; gap /= 2){
        for(int i = gap; i < length; i++){
            for(int j = i - gap; j >= 0 && arr[j] > arr[j + gap]; j -= gap){
                int temp = arr[j];
                arr[j] = arr[j + gap];
                arr[j + gap] = temp;
                count++;
            }
        }
    }
    return count;
}

int main(){    

    int arr[] = {434,312,743,235,897,90,124,431,68,123}; 

    int num = shellsort(arr,10);

    for(int i = 0 ; i < 10; i++){
        printf("%d ",arr[i]);
    }
    printf("\nse ejecuto %d veces",num);

    return 0;
}