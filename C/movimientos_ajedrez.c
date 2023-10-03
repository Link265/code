//movimientos

int movimiento_peon(int x1,int y1,int x2,int y2){

    
    //comprobando si se mueve un espacio hacia adelante
    if(y1 == (y2 + 1)){
        // se comprueba si se mueve en linea recta
        if(x1 == x2){
            //se comprueba si a la posicion donde se desas mover esta vacia
            if(piezas[y2][x2][0] == ' '){
                return 1;
            }
           
        }

        //comprueba si se mueve para atacar un enemigo
        if((x1 == (x2+1)) || (x1 == (x2 - 1)) ){

            if(piezas[y2][x2][1] == '0'){
                return 1;
            }
            
        }
    }

    //comprobando si se mueve 2 posiciones al empezar
    if((y1 == (y2 + 2)) && (x1 == x2) && (y1 == 6)){
        if(piezas[y2][x2][0] == ' '){
            return 1;
        }
    }

    return 0;
}

int movimiento_torre(int x1,int y1, int x2 , int y2){
    //comprobando si se mueve hacia alante o atras
    if((x1 == x2) && (y1 != y2)){
        
        if(y1 < y2){
            
            for(int i = 1; (y1 + i) < y2;i++){
                if(piezas[y1+i][x1][0] != ' '){
                    return 0;
                }
            }
            return 1;
        }else{
            printf("primera condicion Y1:%d Y2:%d X1:%d X2:%d",y1,y2,x1,x2);
            for(int i = 1; (y1 - i) > y2;i++){
                if(piezas[y1 - i][x1][0] != ' '){
                    return 0;
                }
            }
            return 1;
        }
    }

    //comprobando si se mueve lateralmente
    if((y1 == y2) && (x1 != x2)){
        if(x1 < x2){
            for(int i = 1; (x1+i) < x2;i++){
                if(piezas[y1][x1+i][0] != ' '){
                    return 0;
                }
            }
            return 1;
        }else{
            for(int i = 1; (x1 - i) > x2;i--){
                if(piezas[y1][x1-i][0] != ' '){
                    return 0;
                }
            }
            return 1;
        }
    }

    return 0;
}

int movimiento_caballo(int x1,int y1,int x2,int y2){
    
    if(((x1 == (x2 + 2)) || (x1 == (x2 - 2))) && ((y1 == (y2 + 1)) || (y1 == (y2 - 1)))){
        if(piezas[y2][x2][1] != '1'){
            return 1;
        }
        
        return 0;
    }

    if(((x1 == (x2 + 1)) || (x1 == (x2 - 1))) && ((y1 == (y2 + 2)) || (y1 == (y2 - 2)))){
        if(piezas[y2][x2][1] != '1'){
            return 1;
        }
        return 0;
    }

    return 0;
}

int movimiento_alfil(int x1,int y1,int x2,int y2){

    //movimiento al lado inferior derecho
    printf("\n x1:%d, y1:%d, x2:%d, y2:%d \n",x1,y1,x2,y2);
    if((x1 < x2) && (y1 < y2)){
        printf("inferior derecho");
        if((x1 == (x2-1)) && (y1 == (y2-1))){
            if(piezas[y2][x2][1] != '1') return 1;
        }

        for(int i = 1;((x1 + i) < x2) && ((y1 + i) < y2);i++ ){
            if(piezas[y1+i][x1+i][0] != ' ') return 0;

            if(((y1+i) == (y2-1)) && ((x1+i) == (x2-1)) ){
                return 1;
            }
        }
        return 0;
    }

    //movimiento la lado superior izquierdo
    if((x1 > x2) && (y1 > y2)){
        printf("superior izquierdo");
        if((x1 == (x2+1)) && (y1 == (y2+1))){
            
            if(piezas[y2][x2][1] != '1') return 1;
        }

        for(int i = 1;((x1 - i) > x2) && ((y1 - i) > y2);i++ ){
            if(piezas[y1 - i][x1 - i][0] != ' ') return 0;

            if(((y1-i) == (y2+1)) && ((x1-i) == (x2+1)) ){
                return 1;
            }
        }
        return 0;
    }

    //movimiento la lado inferior izquierdo
    if((x1 > x2) && (y1 < y2)){
        printf("inferior izquierdo");
        if((x1 == (x2+1)) && (y1 == (y2- 1))){ 
            if(piezas[y2][x2][1] != '1') return 1;    
        }

        for(int i = 1;((x1 - i) > x2) && ((y1 + i) < y2);i++ ){
            if(piezas[y1 + i][x1 - i][0] != ' ') return 0;

            if(((y1+i) == (y2-1)) && ((x1 - i) == (x2 + 1)) ){
                return 1;
            }
        }
        return 0;
    }

    //movimiento al lado superior derecho
    if((x1 < x2) && (y1 > y2)){
        printf("superior derecho");
        if((x1 == (x2-1)) && (y1 == (y2+1))){
            if(piezas[y2][x2][1] != '1') return 1;
        }

        for(int i = 1;((x1 + i) < x2) && ((y1 - i) > y2);i++ ){
            if(piezas[y1 - i][x1 + i][0] != ' ') return 0;

            if(((y1 - i) == (y2 + 1)) && ((x1 + i) == (x2 - 1)) ){
                return 1;
            }
        }
        return 0;
    }

    return 0;
}

int movimiento_reina(int x1,int y1,int x2,int y2){
    return (movimiento_alfil(x1,y1,x2,y2) || movimiento_torre(x1,y1,x2,y2));
}

int movimiento_rey(int x1,int y1,int x2,int y2){

    //verifica si se mueve hacia los lados o a las esquinas    
    if((y1 == y2+1) || (y1 == y2-1) || (y1 == y2)){
        if(x1 == x2-1){
            return 1;
        }else if((x1 == x2+1)){
            return 1;
        }
    }

    //verifica si se mueve hacia adelante o hacia atras
    if(((y1 == y2+1) || (y1 == y2-1)) && (x1 == x2)){
        return 1;
    }

    return 0;
}

int move(int x1,int y1,int x2,int y2){

    int mov = 0;
    
    if((piezas[y1][x1][0] == 'P') && movimiento_peon(x1,y1,x2,y2))
        mov = 1;
    else if((piezas[y1][x1][0] == 'T') && movimiento_torre(x1,y1,x2,y2))
        mov = 1;
    else if((piezas[y1][x1][0] == 'A') && movimiento_alfil(x1,y1,x2,y2))
        mov = 1;
    else if((piezas[y1][x1][0] == 'C') && movimiento_caballo(x1,y1,x2,y2))
        mov = 1;
    else if((piezas[y1][x1][0] == 'R') && movimiento_reina(x1,y1,x2,y2))
        mov = 1;
    else if((piezas[y1][x1][0] == 'K') && movimiento_rey(x1,y1,x2,y2))
        mov = 1;
    
    if(mov){
        piezas[y2][x2][0] = piezas[y1][x1][0];
        piezas[y2][x2][1] = piezas[y1][x1][1];

        piezas[y1][x1][0] = ' ';
        piezas[y1][x1][1] = '3';
        return 0;
    }
    return 1;
}