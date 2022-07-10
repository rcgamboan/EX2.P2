
# metodo que recibe un caracter y devuelve si este es o no un operandor
def esOperador(c):
    if c == "=>" or c == "ˆ" or c == "&" or c == "|" or c == "(" or c == ")":
        return True
    return False

# metodo que recibe un caracter y devuelve si este es o no un operando
def esOperando(valor):
    if valor == "true" or valor == "false":
        return True
    return False

# Funcion para evaluar expresiones escritas en orden pre-fijo
# Se simula el uso de una pila para realizar la evaluacion
# Recibe una lista con los operadores y operandos de la expresion a evaluar
def evalPrefix(expresion):


    if len(expresion) == 1:
        if expresion[0] == "true" or expresion[0] == "false":
            return expresion[0]
        else:
            print("error al evaluar la expresion")
    else:
        if esOperando(expresion[0]):
            print("la expresion no se encuentra escrita en orden pre-fijo")
            return None

    pila = []

    # Como la expresion esta escrita en orden pre-fijo
    # se realiza un ciclo for desde el ultimo elemento hasta el primero de la expresion
    # e inicialmente se agregan los operandos a la pila hasta conseguir el primer operador
    # al encontrar el primer operador se hace pop a la pila de dos elementos si el operador es binario
    # o un solo elemento si el operador es unario
    # luego se evalua el o los operandos con el respectivo operador y se agrega el resultado a la pila
    for j in range(len(expresion)-1, -1, -1):
                  
        # Se verifica si el elemento actual es un operando o un operador
        # Si se trata de un operando se agrega a la "pila"
        if esOperando(expresion[j]):
           
            pila.append(expresion[j])

        elif esOperador(expresion[j]):
            # Se extraen los operandos de la pila
            if expresion[j] == 'ˆ':
                o1 = pila[-1]
                pila.pop()
            else:
                o2 = pila.pop()
                o1 = pila.pop()
 
            # Se verifica que operador se encontro y se evalua la expresion
            if expresion[j] == '|':
                if o1 == "true" or o2 == "true":
                    pila.append("true")
                else:
                    pila.append("false")
            elif expresion[j] == '&':
                if o1 == "false" or o2 == "false":
                    pila.append("false")
                else:
                    pila.append("true")
            elif expresion[j] == '=>':
                if o1 == "true" and o2 == "false":
                    pila.append("false")
                else:
                    pila.append("true")
            elif expresion[j] == 'ˆ':
                if o1 == "true":
                    pila.append("false")
                else:
                    pila.append("true")
        else:
            print("error en la expresion")
            return None
                 
    return pila.pop()

# Funcion para evaluar expresiones escritas en orden post-fijo
# Se simula el uso de una pila para realizar la evaluacion
# Recibe una lista con los operadores y operandos de la expresion a evaluar
def evalPostfix(expresion):

    
    if len(expresion) == 1:
        if expresion[0] == "true" or expresion[0] == "false":
            return expresion[0]
        else:
            print("error al evaluar la expresion")
    else:
        if not esOperando(expresion[0]):
            print("la expresion no se encuentra escrita en orden post-fijo")
            return None

    pila = []

    # Como la expresion esta escrita en orden post-fijo
    # se realiza un ciclo for sobre los elementos de la expresion
    # e inicialmente se agregan los operandos a la pila hasta conseguir el primer operador
    # al encontrar el primer operador se hace pop a la pila de dos elementos si el operador es binario
    # o un solo elemento si el operador es unario
    # luego se evalua el o los operandos con el respectivo operador y se agrega el resultado a la pila
    for i in expresion:

        if esOperando(i):
            pila.append(i)
        elif esOperador(i):

            if i != 'ˆ':
                operando2 = pila.pop()
                operando1 = pila.pop()
            else:
                operando1 = pila.pop()
            
            if i == 'ˆ':
                #print("ˆ"+operando1)
                if operando1 == "true":
                    pila.append("false")
                else:
                    pila.append("true")
            elif i == "=>":
                #print(operando1 + "=>" + operando2)
                if operando1 == "true" and operando2 == "false":
                    pila.append("false")
                else:
                    pila.append("true")
            elif i == '&':
                #print(operando1 + "&" + operando2)
                if operando1 == "true" and operando2 == "true":
                    pila.append("true")
                else:
                    pila.append("false")
            elif i == '|':
                #print(operando1 + "|" + operando2)
                if operando1 == "false"  and operando2 == "false":
                    pila.append("false")
                else:
                    pila.append("true")
        else:
            print("error en la expresion")
            return None
    return pila.pop()

