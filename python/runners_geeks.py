#mueve los caracteres una posicion antes 
def move_before(string,original_position):
    new_string = f"{string[:original_position-1]}{string[original_position]}{string[original_position-1]}{string[original_position+1:]}"
    return new_string

#mueve los caractere un posicion despues
def move_after(string,original_position):
    new_string = f"{string[:original_position]}{string[original_position+1]}{string[original_position]}{string[original_position+2:]}"
    return new_string

def post_order(string):
    pass
    
def compare(a):
    if (a == '+') or (a == '-') or (a == '*') or (a == '/' or (a == '^')):
        return True
    return False



def pre_order(string):

    for i in range(1,len(string)):

        if string[i] == '*' or string[i] == '/':

            if string[i-1] == ')':

                posicion_actual = i

                parentesis_cerrado = False

                while (posicion_actual != 0) and (not parentesis_cerrado or (string[posicion_actual-1] == '^')):
                    if string[posicion_actual+1] == '(':
                        parentesis_cerrado = True
                    string = move_before(string,posicion_actual)
                    posicion_actual -= 1
            else:
                string = move_before(string,i)        

        


        

    