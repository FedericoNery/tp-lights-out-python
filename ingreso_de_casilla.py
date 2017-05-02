def validacionIngresoDeCasillero(dimension_tablero):
    """Recibe el parametro que indica la dimension del tablero. El usuario procede al ingreso de la casilla, luego
    se verifica que la casilla pertenezca al tablero y que el ingreso no sea erroneo (mas caracteres o la inversion
    del orden de ingreso letra-numero(numero-letra)"""
    validacion=False
    dimension_fila=str(chr(dimension_tablero+48))
    dimension_columna=str(chr(dimension_tablero+64))

    while(validacion==False):
        casilla = input("Ingrese la casilla de la luz que desea apagar o escriba \"reinicio\" para volver al inicio del nivel ")
        casilla = casilla.upper()
        if(len(casilla)==2):
            if((casilla[0]>='A') and (casilla[0]<=dimension_columna)):
                if((casilla[1]>='1') and (casilla[1]<=dimension_fila)):
                    validacion=True
                    return (casilla)
                else:
                    validacion = False
                    print ("Error ")
            else:
                validacion = False
                print ("Error ")
        elif(casilla=="REINICIO"):
            return (casilla)
        else:
            validacion= False
            print ("Error ")
