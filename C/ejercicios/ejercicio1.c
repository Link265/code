 #include <stdio.h>

 int main(){

   printf("ingrese un numero: ");
   int num;
   scanf("%d",&num);


   int factores[100];
   int numero_de_factores = 0;
   int divisor = 2;
   while(1){

      if(divisor>num){
         break;
      }
      
      if( (num%divisor) == 0){
         factores[numero_de_factores] = divisor;
         num /= divisor;
         divisor = 2;
         numero_de_factores++;
         continue;
      }

      divisor++;
   }
   printf("los factores primos son: ");

   for (int i = 0; i < numero_de_factores; i++){
      printf("%d ",factores[i]);
   }
    

   return 0;
 }