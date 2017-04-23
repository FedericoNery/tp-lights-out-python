def validacionIngresoDeCasillero(dimension_tablero):
    """Recibe el parametro que indica la dimension del tablero. El usuario procede al ingreso de la casilla, luego
    se verifica que la casilla pertenezca al tablero y que el ingreso no sea erroneo (mas caracteres o la inversion
    del orden de ingreso letra-numero(numero-letra)"""
    validacion=False
    while(validacion==False):
        casilla = raw_input("Ingrese la casilla de la luz que desea apagar ")
        casilla = casilla.upper()
        if(len(casilla)==2):
            if((casilla[0]>='A') and (casilla[0]<='Z')):
                if((casilla[1]>='1') and (casilla[1]<='9')):
                    validacion=True
                    return (casilla)
                else:
                    validacion = False
                    print ("Error ")
            else:
                validacion = False
                print ("Error ")
        else:
            validacion= False
            print ("Error ")
validacionIngresoDeCasillero(0)