def modificoTablero(tablero, ingresoCoordenadaDelUsuario):
    #Cuatro casilleros alrededor del central
    filaCasillaCentral = ingresoCoordenadaDelUsuario[1]
    columnaCasillaCentral = ingresoCoordenadaDelUsuario[0]

    casillaALaIzquierda = chr(ord(columnaCasillaCentral) - 1) + filaCasillaCentral
    casillaALaDerecha = chr(ord(columnaCasillaCentral) + 1) + filaCasillaCentral
    casillaSuperior = columnaCasillaCentral + str(int(filaCasillaCentral) - 1)
    casillaInferior = columnaCasillaCentral + str(int(filaCasillaCentral) + 1)

    casillasConPosiblesCambiosDeEstado = [ingresoCoordenadaDelUsuario,casillaALaIzquierda,casillaALaDerecha,casillaSuperior,casillaInferior]

    for coordenada in casillasConPosiblesCambiosDeEstado:
        if(coordenada in tablero):

            if(tablero.get(coordenada,[]) == 'O'):
                tablero[coordenada] = '.'

            else:
                tablero[coordenada] = 'O'

    return (tablero)