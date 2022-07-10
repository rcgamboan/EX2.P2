import eval
import mostrar
import sys

# cliente que usa las funciones definidas en eval y mostrar
# para trabajar con expresiones booleanas

print("\n\nCliente para evaluar y mostrar expresiones booleanas")
print("\nA continuacion indique la operacion que quiere realizar")
print("\nLas operaciones disponibles son las siguientes: ")
print("\nEVAL    <orden> <expr>        Representa una evaluacion de la expresion en <expr>, que esta escrita de acuerdo a <orden>.")
print("\nMOSTRAR <orden> <expr>        Representa una impresion en orden infijo de la expresion en <expr>, que esta escrita de acuerdo a <orden>.")
print("\nSALIR                         Termina la ejecucion del programa\n")
while True:

    comando = input("main> ")

    if comando == '':
        continue

    argumentos = comando.split()

    if argumentos[0] == "SALIR" or argumentos[0] == "salir":
        print("Se termina la ejecucion del programa")
        sys.exit()
    elif argumentos[0] == "EVAL" or argumentos[0] == "eval":
        
        if len(argumentos) < 3:
            print("Formato invalido.")
        else:
            expresion = argumentos[2:]
            
            if argumentos[1] == "PRE" or argumentos[1] == "pre":
                print(eval.evalPrefix(expresion))
            elif argumentos[1] == "POST" or argumentos[1] == "post":
                print(eval.evalPostfix(expresion))
            else:
                print("error con el orden de la expresion")
            
            
    elif argumentos[0] == "MOSTRAR" or argumentos[0] == "mostrar":

        if len(argumentos) < 3:
            print("Formato invalido.")
        else:
            expresion = argumentos[2:]
            if argumentos[1] == "PRE" or argumentos[1] == "pre":
                print(mostrar.preFijoaInfijo(expresion))
            elif argumentos[1] == "POST" or argumentos[1] == "post":
                print(mostrar.postFijoaInfijo(expresion))
            else:
                print("error con el orden de la expresion")
                
            
    else:
        print("Operacion no valida\n")

    