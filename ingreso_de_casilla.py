def validacionIngresoDeCasillero(dimension_tablero):
    """Recibe el parametro que indica la dimension del tablero. El usuario procede al ingreso de la casilla, luego
    se verifica que la casilla pertenezca al tablero y que el ingreso no sea erroneo (mas caracteres o la inversion
    del orden de ingreso letra-numero(numero-letra)"""
    ingresoDeCoordenada=False
    dimension_fila=str(chr(dimension_tablero+48))
    dimension_columna=str(chr(dimension_tablero+64))

    while(not ingresoDeCoordenada):
        coordenadaDelUsuario = input("Ingrese la casilla de la luz que desea apagar o escriba \"reinicio\" para volver al inicio del nivel ")
        coordenadaDelUsuario = coordenadaDelUsuario.upper()
        if(longitudDeCoordenadaValida(coordenadaDelUsuario)):
            if(letraDeCoordenadaValida(coordenadaDelUsuario,dimension_columna)):
                if(numeroDeCoordenadaValida(coordenadaDelUsuario,dimension_fila)):
                    ingresoDeCoordenada=True
                    return (coordenadaDelUsuario)
                else:
                    ingresoDeCoordenada = False
                    print ("Error ")
            else:
                ingresoDeCoordenada = False
                print ("Error ")
        elif(ingresoDeCoordenadaEsReinicio(coordenadaDelUsuario)):
            return (coordenadaDelUsuario)
        else:
            ingresoDeCoordenada= False
            print ("Error ")

def longitudDeCoordenadaValida(coordenadaDelUsuario):
    return (len(coordenadaDelUsuario) == 2)

def ingresoDeCoordenadaEsReinicio(coordenadaDelUsuario):
    return (coordenadaDelUsuario == "REINICIO")

def letraDeCoordenadaValida(coordenadaDelUsuario,dimension_columna):
    return ((coordenadaDelUsuario[0]>= 'A') and (coordenadaDelUsuario[0]<=dimension_columna))

def numeroDeCoordenadaValida(coordenadaDelUsuario,dimension_fila):
    return ((coordenadaDelUsuario[1]>= '1') and (coordenadaDelUsuario[1]<=dimension_fila))