def esOperador(c):
    if c == "=>" or c == "ˆ" or c == "&" or c == "|" or c == "(" or c == ")":
        return True
    return False

def esOperando(valor):
    if valor == "true" or valor == "false":
        return True
    return False


def preFijoaInfijo(expresion):
    stack = []
     
    # se lee la expresion desde el final hasta el inicio
    i = len(expresion) - 1
    while i >= 0:

        # si se consigue un operando, se agrega a la pila
        if esOperando(expresion[i]):
             
            stack.append(expresion[i])
            i -= 1
        elif esOperador(expresion[i]):
            
            if i == "ˆ":
                op1 = stack.pop()  
                stack.append(expresion[i] + op1)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if expresion[i] == "=>":
                    stack.append( "(" + op1 + expresion[i] + op2 + ")")    
                else:
                    
                    stack.append( op1 + " " + expresion[i] + " " + op2)

            i -= 1
     
    return stack.pop()

 
def postFijoaInfijo(expresion) :
    s = []
 
    for i in expresion:    

        if esOperando(i) :        
            s.append(i)
        elif esOperador(i):
            
            if i == "ˆ":
                op1 = s.pop()  
                s.append(i + op1)
            else:
                
                op1 = s.pop()
                op2 = s.pop()
                if i == "=>":
                    s.append( "(" + op2 + i + op1 + ")")    
                else:
                    s.append( op2 + " " + i + " " + op1)
             
    return s.pop()
 
"""
pre = "| & => true true false true"
print(preFijoaInfijo(pre))
post = "true false => false | true false ˆ | &"
print(postFijoaInfijo(post))
"""