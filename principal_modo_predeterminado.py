import niveles_predeterminados
import mostrar_tablero
import calculo_de_puntaje
import mensajes_del_juego
import logica_del_juego
import ingreso_de_casilla
import menu_de_inicio
import modificadorTablero

def principalPredeterminado(dimensionDelTablero):
    nivelDelJuego = 1
    reinicioDelJuego = False
    ganoJuego = False
    puntajeActual = 0
    movimientosIniciales = 0
    puntajesPorNivel = [0,0,0,0,0]
    contadorNivel = 0

    while(logica_del_juego.noSeGanoElJuego(nivelDelJuego,ganoJuego)):

        print("NIVEL " + str(nivelDelJuego)+"\n")
        ganaNivel = None
        lucesRestantes = 0
        tablero = niveles_predeterminados.niveles_predeterminados(nivelDelJuego)
        mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
        movimientosRestantes = dimensionDelTablero * 3
        movimientosIniciales = movimientosRestantes
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
        lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

        while(logica_del_juego.noSeGanoElNivel(movimientosRestantes,ganaNivel,lucesRestantes)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(dimensionDelTablero)

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)
                reinicioDelJuego = True
                tablero = logica_del_juego.restablezcoTableroOriginalPredeterminado(nivelDelJuego)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = dimensionDelTablero * 3
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
                puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
                puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
                calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel, nivelDelJuego)
                calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
                reinicioDelJuego = False
            else:
                tablero = modificadorTablero.modificoTablero(tablero,coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = movimientosRestantes-1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

                if(logica_del_juego.noQuedanLucesPrendidas(lucesRestantes)):
                    ganaNivel = True
                elif(logica_del_juego.siQuedanLucesPrendidasYNoQuedanMovimientos(lucesRestantes,movimientosRestantes)):
                    ganaNivel = False

        if(ganaNivel):
            mensajes_del_juego.mensajeGanoNivel()
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel,reinicioDelJuego,lucesRestantes)
            puntajesPorNivel[nivelDelJuego-1] = puntajeActual+puntajesPorNivel[nivelDelJuego-1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel,nivelDelJuego)

            if(nivelDelJuego == 5):
                ganoJuego = True
            else:
                nivelDelJuego = nivelDelJuego+1

        if(logica_del_juego.perdioElNivel(movimientosRestantes,ganaNivel)):
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
            puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            print("\n")
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)

            mensajes_del_juego.mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (ganoJuego):
        print("\n")
        calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)
        mensajes_del_juego.mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()