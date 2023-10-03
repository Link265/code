//input

void limpiar(){
    char c;
    while (((c = getchar()) != '\n') && c != EOF);
}

int validacion(int a){
    if(a > 0 && a < 9){
        return 0;
    }
    printf("posicion invalida \n");
    return 1;
}

char conver_mayus(char a){
    if(a >= 'a' && a <= 'z'){
        a -= 32;
    }else if(a < 'A' || a > 'Z'){
        a = '0';
    }
    return a;
}

int num_de_letra(char a){
    switch(a){
        case 'A': return 0;
        case 'B': return 1;
        case 'C': return 2;
        case 'D': return 3;
        case 'E': return 4;
        case 'F': return 5;
        case 'G': return 6;
        case 'H': return 7;
        default: return -1;
    }
}

void input(){
    int fila1;
    int fila2;
    char columna1;
    char columna2;

    while(1){
        printf("escriba el numero de la fila de la pieza que desee mover: ");
        scanf("%d",&fila1);  limpiar();
        if(validacion(fila1)){
            continue;
        }
        fila1--;
        fila1 = 7 - fila1;

        printf("escriba la letra de la columna de la pieza que desee mover: ");
        scanf("%c",&columna1); limpiar();
        columna1 = conver_mayus(columna1);
        if(columna1 == '0'){
            printf("posicion invalida\n");
            continue;
        }

        printf("escriba la fila a donde desea mover la pieza: ");
        scanf("%d",&fila2); limpiar();
        if(validacion(fila2)){
            continue;
        }
        fila2--;
        fila2 = 7 - fila2;

        printf("escriba la columna a donde desea mover la pieza: ");
        scanf("%c",&columna2); limpiar();
        columna2 = conver_mayus(columna2);
        if(columna2 == '0'){
            printf("posicion invalida\n");
            continue;
        }

        int error = move(num_de_letra(columna1),fila1,num_de_letra(columna2),fila2);

        if(!error){
            break;
        }else{
            printf("movimiento invalido\n");
        }
    }
}