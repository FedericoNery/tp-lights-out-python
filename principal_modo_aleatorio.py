import niveles_aleatorios
import mostrar_tablero
import ingreso_de_casilla
import calculo_de_puntaje
import modificadorTablero
import mensajes_del_juego
import logica_del_juego
import menu_de_inicio

def principalAleatorio(dimensionDelTablero):
    nivelDelJuego = 1
    reinicioDelJuego = False
    ganoJuego=False
    puntajeActual = 0
    movimientosIniciales = 0
    tuplaPuntajes = ()
    puntajesPorNivel = [0,0,0,0,0]
    contadorNivel = 0
    tableroOriginal={}

    while (nivel <= 5):
        ganaNivel = None
        lucesRestantes = 0
        tablero = niveles_aleatorios.generarTableroAleatorio(dimensionDelTablero)
        tableroOriginal = tablero.copy()
        mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
        movimientosRestantes = dimensionDelTablero*3
        movimientosIniciales = movimientosRestantes
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
        lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

        while((movimientosRestantes > 0) and (ganaNivel == None) and (lucesRestantes > 0)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(dimensionDelTablero)

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)
                reinicioDelJuego = True
                puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)

                movimientosRestantes = dimensionDelTablero * 3
                tablero = tableroOriginal
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))

            else:
                tablero = modificadorTablero.modificoTablero(tablero, coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = movimientosRestantes - 1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

                if(lucesRestantes == 0):
                    ganaNivel = True

                elif((lucesRestantes == 0) and (movimientosRestantes == 0)):
                    ganaNivel = False

        if (ganaNivel == True):
            mensajes_del_juego.mensajeGanoNivel()
            #muestroEnPantallaLosPuntajes(tuplaPuntajes, ganaNivel, nivel, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
            if (nivel == 5):
                ganoJuego = True
            else:
                nivel = nivel + 1

        if ((movimientosRestantes == 0) and (ganaNivel == False)):

            #muestroEnPantallaLosPuntajes(tuplaPuntajes, ganaNivel, nivel, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
            ganaNivel = None
            tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(ganaNivel, nivel, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
            print("")
            print("TABLA DE PUNTAJES FINALES: ")
            print("El puntaje total es de: " + str(tuplaPuntajes[1]))
            tuplaPuntajes = tuplaPuntajes[2]
            for i in tuplaPuntajes:
                contadorNivel = contadorNivel + 1
                print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))
            mensajes_del_juego.mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (ganoJuego == True):
        ganaNivel = None
        #tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(ganaNivel, nivel, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
        print("El puntaje total es de: "+ str(tuplaPuntajes[2]))
        tuplaPuntajes = tuplaPuntajes[2]
        for i in tuplaPuntajes:
            contadorNivel = contadorNivel+1
            print("El puntaje obtenido en el nivel "+str(contadorNivel)+" es de "+str(i))
        mensajes_del_juego.mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()