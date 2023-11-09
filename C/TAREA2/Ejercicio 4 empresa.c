#include <stdio.h>

#define MONITOR 101
#define MONITOR_PRECIO_COSTO 158.45
#define MONITOR_PRECIO_VENTA 206

#define IPHONE 110
#define IPHONE_PRECIO_COSTO 958.22
#define IPHONE_PRECIO_VENTA 1022.5

#define NESPRESSO 111
#define NESPRESSO_PRECIO_COSTO 368.89
#define NESPRESSO_PRECIO_VENTA 430.33

#define COMPRA 'C'
#define VENTA 'V'
#define GARANTIA 'G'
#define DEVOLUCION 'D'

float perdidas = 0;
float ganancias = 0;
int devoluciones = 0;

void operar(char operacion,int * catidad,float precio_costo,float precion_venta );

void operar(char operacion,int * cantidad,float precio_costo,float precion_venta ){

    switch(operacion){
    case COMPRA:
        (*cantidad)++;
        ganancias -= precio_costo;
        break;
    case VENTA:
        (*cantidad)--;
        ganancias += precion_venta;
        break;
    case GARANTIA:
        (*cantidad)--;
        perdidas += precio_costo;
        break;
    case DEVOLUCION:
        (*cantidad)++;
        ganancias -= precion_venta;
        devoluciones++;
        break;                
    }
} 

int main(){

    int cantidad_monitor = 12;
    int cantidad_iphone = 3;
    int cantidad_nespresso = 20;

    int codigo,cantidad;// variables que se van a 
    char operacion;// obtener de un archivo

    FILE * movimentos_octubre = fopen("movimientos_octubre.txt","r");
    FILE * stock_octubre = fopen("stock_octubre.txt","w");
    if(movimentos_octubre == NULL || stock_octubre == NULL){
        printf("error abriendo archivos");
        return 1; 
    }

    while((fscanf(movimentos_octubre,"%d",&codigo)) != EOF){

        fscanf(movimentos_octubre,"%d",&cantidad);
        fscanf(movimentos_octubre,"%c",&operacion);

        switch (codigo){
        case MONITOR:
            operar(operacion,&cantidad_monitor,MONITOR_PRECIO_COSTO,MONITOR_PRECIO_VENTA);
            break;
        case IPHONE:
            operar(operacion,&cantidad_iphone,IPHONE_PRECIO_COSTO,IPHONE_PRECIO_VENTA);
            break;
        case NESPRESSO:
            operar(operacion,&cantidad_nespresso,NESPRESSO_PRECIO_COSTO,NESPRESSO_PRECIO_VENTA);
            break;        
        default:
            continue;
            break;
        }
    }
    fclose(movimentos_octubre);

    fprintf(stock_octubre,"MONITOR SAMSUNG 27\" %d %.2f\n",cantidad_monitor,cantidad_monitor * MONITOR_PRECIO_COSTO);
    fprintf(stock_octubre,"IPHONE 15 PRO %d %.2f\n",cantidad_iphone,cantidad_iphone * IPHONE_PRECIO_COSTO);
    fprintf(stock_octubre,"MAQUINA NESPRESSO NEGRA %d %.2f\n",cantidad_nespresso,cantidad_nespresso * NESPRESSO_PRECIO_COSTO);

    fprintf(stock_octubre,"Monto total de perdida por garantia: %.2f\n",perdidas);
    fprintf(stock_octubre,"Monto total de ganancias de ventas: %.2f\n",ganancias);
    fprintf(stock_octubre,"Cantidad de productos devueltos: %d",devoluciones);

    fclose(stock_octubre);

    return 0;
}