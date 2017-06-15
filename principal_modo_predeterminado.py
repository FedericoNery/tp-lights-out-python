import niveles_predeterminados
import mostrar_tablero
import calculo_de_puntaje
import mensajes_del_juego
import logica_del_juego
import ingreso_de_casilla
import menu_de_inicio
import modificador_tablero

def principalPredeterminado(dimensionDelTablero):
    nivelDelJuego = 1
    reinicioDelJuego = False
    ganoJuego = False
    puntajesPorNivel = [0,0,0,0,0]

    while(logica_del_juego.noSeGanoElJuego(nivelDelJuego,ganoJuego)):

        print("NIVEL " + str(nivelDelJuego)+"\n")
        ganaNivel = None
        tablero = niveles_predeterminados.niveles_predeterminados(nivelDelJuego)
        mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
        movimientosRestantes = dimensionDelTablero * 3
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(dimensionDelTablero*3))
        lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

        while(logica_del_juego.noSeGanoElNivel(movimientosRestantes,ganaNivel,lucesRestantes)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(dimensionDelTablero)

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)
                tablero = logica_del_juego.restablezcoTableroOriginalPredeterminado(nivelDelJuego)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = dimensionDelTablero * 3
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(dimensionDelTablero * 3))
                puntajesPorNivel[nivelDelJuego - 1] += calculo_de_puntaje.calcularPuntajePorReinicio(lucesRestantes)
                calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel, nivelDelJuego)
                calculo_de_puntaje.imprimirPuntajeTotal(puntajesPorNivel)
            else:
                tablero = modificador_tablero.modificoTablero(tablero, coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = movimientosRestantes - 1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(dimensionDelTablero * 3))
                lucesRestantes = logica_del_juego.calculoDeLucesRestantes(tablero)

        if(logica_del_juego.noQuedanLucesPrendidas(lucesRestantes)):
            ganaNivel = True
            mensajes_del_juego.mensajeGanoNivel()
            puntajesPorNivel[nivelDelJuego-1] += calculo_de_puntaje.calculoPuntajeActual(ganaNivel)
            calculo_de_puntaje.imprimirPuntajeTotal(puntajesPorNivel)
            calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel,nivelDelJuego)

            if(not logica_del_juego.ganoElJuego(nivelDelJuego,lucesRestantes)):
                nivelDelJuego = nivelDelJuego+1
            else:
                ganoJuego = True

        if(logica_del_juego.perdioElNivel(movimientosRestantes,ganaNivel)):
            ganaNivel = False
            puntajesPorNivel[nivelDelJuego - 1] += calculo_de_puntaje.calculoPuntajeActual(ganaNivel)
            print("\n")
            calculo_de_puntaje.imprimirPuntajeTotal(puntajesPorNivel)
            calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)

            mensajes_del_juego.mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (logica_del_juego.ganoElJuego(nivelDelJuego,lucesRestantes)):
        print("\n")
        calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel)
        mensajes_del_juego.mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()