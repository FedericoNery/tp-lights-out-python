import error_logger
numeroUltimaFilaDelTablero = ""
letraUltimaColumnaDelTablero = ""


def validacionIngresoDeCasillero(dimensionTablero):
    """Recibe el parametro que indica la dimension del tablero. El usuario procede al ingreso de la casilla, luego
    se verifica que la casilla pertenezca al tablero y que el ingreso no sea erroneo (mas caracteres o la inversion
    del orden de ingreso letra-numero(numero-letra)"""
    global numeroUltimaFilaDelTablero,letraUltimaColumnaDelTablero
    ingresoDeCoordenada = False
    numeroUltimaFilaDelTablero = str(chr(dimensionTablero + 48))
    letraUltimaColumnaDelTablero = str(chr(dimensionTablero + 64))

    while(not ingresoDeCoordenada):
        coordenadaDelUsuario = input("Ingrese la casilla de la luz que desea apagar o escriba \"reinicio\" para volver al inicio del nivel ")
        coordenadaDelUsuario = coordenadaDelUsuario.upper()

        if(longitudDeCoordenadaValida(coordenadaDelUsuario) and letraDeCoordenadaValida(coordenadaDelUsuario) and numeroDeCoordenadaValida(coordenadaDelUsuario)):
            ingresoDeCoordenada = True
            return (coordenadaDelUsuario)

        elif(ingresoDeCoordenadaEsReinicio(coordenadaDelUsuario)):
            return (coordenadaDelUsuario)

        else:
            ingresoDeCoordenada = False
            error_logger.guardar('Se ingreso mal la coordenada del tablero o la opcion de "Reinicio" . Valor de Ingreso: '+ coordenadaDelUsuario)
            print ("Error ")

def longitudDeCoordenadaValida(coordenadaDelUsuario):
    return (len(coordenadaDelUsuario) == 2)

def ingresoDeCoordenadaEsReinicio(coordenadaDelUsuario):
    return (coordenadaDelUsuario == "REINICIO")

def letraDeCoordenadaValida(coordenadaDelUsuario):
    return ((coordenadaDelUsuario[0] >= 'A') and (coordenadaDelUsuario[0] <= letraUltimaColumnaDelTablero))

def numeroDeCoordenadaValida(coordenadaDelUsuario):
    return ((coordenadaDelUsuario[1] >= '1') and (coordenadaDelUsuario[1] <= numeroUltimaFilaDelTablero))

