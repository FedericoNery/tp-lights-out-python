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
    puntajesPorNivel = [0,0,0,0,0]
    tableroOriginal = {}

    while (logica_del_juego.noSeGanoElJuego(nivelDelJuego,ganoJuego)):

        print("NIVEL " + str(nivelDelJuego) + "\n")
        ganaNivel = None
        lucesRestantes = 0
        tablero = niveles_aleatorios.generarTableroAleatorio(dimensionDelTablero)
        tableroOriginal = tablero.copy()
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
                tablero = tableroOriginal
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = dimensionDelTablero * 3
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
                puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
                puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
                calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel, nivelDelJuego)
                calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
                reinicioDelJuego = False
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)


            else:
                tablero = modificadorTablero.modificoTablero(tablero, coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = movimientosRestantes - 1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

        if (logica_del_juego.noQuedanLucesPrendidas(lucesRestantes)):
            ganaNivel = True
            mensajes_del_juego.mensajeGanoNivel()
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
            puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel, nivelDelJuego)

            if (not logica_del_juego.ganoElJuego(nivelDelJuego, lucesRestantes)):
                nivelDelJuego = nivelDelJuego + 1
            else:
                ganoJuego = True

        if (logica_del_juego.perdioElNivel(movimientosRestantes, ganaNivel)):
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
            puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            print("\n")
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)

            mensajes_del_juego.mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (logica_del_juego.ganoElJuego(nivelDelJuego,lucesRestantes)):
        print("\n")
        calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)
        mensajes_del_juego.mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()