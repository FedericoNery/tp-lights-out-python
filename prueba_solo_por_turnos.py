import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios
import calculo_de_puntaje
import sys

def verificoReinicio(numeroDelNivel, dimensionDelTablero):
     tablero = niveles_predeterminados.niveles_predeterminados(numeroDelNivel)
     mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
     movimientosRestantes = dimensionDelTablero * 3
     return (tablero, movimientosRestantes)

def calculoDeLucesRestantes(tablero):
    cantidadDeLucesRestantes = 0
    estadosDeLucesDelTablero = tablero.values()
    for estadoDeLuz in estadosDeLucesDelTablero:
        if (estadoDeLuz == 'O'):
            cantidadDeLucesRestantes = cantidadDeLucesRestantes + 1
    return (cantidadDeLucesRestantes)

def noSeGanoElJuego(nivelDelJuego,ganoJuego):
    return ((nivelDelJuego<=5) and (not ganoJuego))

def muestroEnPantallaLosPuntajes(ganaNivel,nivel,reinicioElJuego,lucesRestantes,puntajesPorNivel):
    puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel,reinicioElJuego,lucesRestantes)
    puntajesPorNivel[nivel-1]=puntajesPorNivel[nivel-1]+puntajeActual
    puntajeTotal=calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
    print("El puntaje en el nivel es: " + str(puntajesPorNivel[nivel-1]))
    print("El puntaje total es de : " + str(puntajeTotal))


def mensajeGanoJuego():
    print("""
      G G G      A     NN    N   O O O      E E E  L        J J J U     U  E E E   G G G   O O O
     G          A A    N N   N  O     O     E      L          J   U     U  E      G       O     O
     G   G G   A   A   N  N  N  O     O     E E E  L          J   U     U  E E E  G   G G O     O
     G     G  A A A A  N   N N  O     O     E      L          J   U     U  E      G     G O     O
      G G G  A       A N    NN   O O O      E E E  L L L   J J     U U U   E E E   G G G   O O O
    """)

def mensajeGanoNivel():
    print("""
             G G G      A     NN    N   O O O      E E E  L        NN    N  I  V       V  E E E  L
            G          A A    N N   N  O     O     E      L        N N   N  I   V     V   E      L
            G   G G   A   A   N  N  N  O     O     E E E  L        N  N  N  I    V   V    E E E  L
            G     G  A A A A  N   N N  O     O     E      L        N   N N  I     V V     E      L
             G G G  A       A N    NN   O O O      E E E  L L L    N    NN  I      V      E E E  L L L
            """)
    return ("")

def mensajePerdiste():
    print("""
           P P P   E E E  R R R    D D D   I   S S S  T T T  E E E
           P    P  E      R    R   D    D  I  S         T    E
           P P P   E E E  R R R    D    D  I    S S     T    E E E
           P       E      R    R   D    D  I       S    T    E
           P       E E E  R     R  D D D   I  S S S     T    E E E
           """)
    return ("")

def noSeGanoElNivel(movimientosRestantes,gananivel,lucesRestantes):
    return ((movimientosRestantes > 0) and (gananivel == None) and (lucesRestantes > 0))

def perdioElNivel(movimientosRestantes,gananivel):
    return ((movimientosRestantes == 0) and (gananivel == False))

def noQuedanLucesPrendidas(lucesRestantes):
    return lucesRestantes == 0

def siQuedanLucesPrendidasYNoQuedanMovimientos(lucesRestantes,movimientosRestantes):
    return ((lucesRestantes > 0) and (movimientosRestantes == 0))

def principalPredeterminado(dimensionDelTablero):
    nivelDelJuego = 1
    reinicioDelJuego = False
    ganoJuego = False
    puntajeActual = 0
    movimientosIniciales = 0
    tableroYMovimientosRestantes = ()
    puntajesPorNivel = [0,0,0,0,0]
    contadorNivel = 0

    while(noSeGanoElJuego(nivelDelJuego,ganoJuego)):

        print("NIVEL " + str(nivelDelJuego)+"\n")
        ganaNivel = None
        lucesRestantes = 0
        tablero = niveles_predeterminados.niveles_predeterminados(nivelDelJuego)
        mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
        movimientosRestantes = dimensionDelTablero * 3
        movimientosIniciales = movimientosRestantes
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
        lucesRestantes = calculoDeLucesRestantes(tablero)

        while(noSeGanoElNivel(movimientosRestantes,ganaNivel,lucesRestantes)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(dimensionDelTablero)

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = calculoDeLucesRestantes(tablero)
                tableroYMovimientosRestantes = verificoReinicio(nivelDelJuego , dimensionDelTablero)
                reinicioDelJuego = True
                tablero = tableroYMovimientosRestantes[0]
                movimientosRestantes = tableroYMovimientosRestantes[1]
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
                lucesRestantes = calculoDeLucesRestantes(tablero)

                if(noQuedanLucesPrendidas(lucesRestantes)):
                    ganaNivel = True
                elif(siQuedanLucesPrendidasYNoQuedanMovimientos(lucesRestantes,movimientosRestantes)):
                    ganaNivel = False

        if(ganaNivel):
            mensajeGanoNivel()
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel,reinicioDelJuego,lucesRestantes)
            puntajesPorNivel[nivelDelJuego-1] = puntajeActual+puntajesPorNivel[nivelDelJuego-1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirPuntajeDelNivel(puntajesPorNivel,nivelDelJuego)

            if(nivelDelJuego == 5):
                ganoJuego = True
            else:
                nivelDelJuego = nivelDelJuego+1

        if(perdioElNivel(movimientosRestantes,ganaNivel)):
            puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)
            puntajesPorNivel[nivelDelJuego - 1] = puntajeActual + puntajesPorNivel[nivelDelJuego - 1]
            puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
            ganaNivel = None
            calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
            calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel, contadorNivel)

            mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (ganoJuego):
        puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel,reinicioDelJuego,lucesRestantes)
        puntajeTotal = calculo_de_puntaje.calculoPuntajeTotal(puntajesPorNivel)
        calculo_de_puntaje.imprimirPuntajeTotal(puntajeTotal)
        calculo_de_puntaje.imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel,contadorNivel)

        mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()

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
        lucesRestantes = calculoDeLucesRestantes(tablero)

        while((movimientosRestantes > 0) and (ganaNivel == None) and (lucesRestantes > 0)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(dimensionDelTablero)

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = calculoDeLucesRestantes(tablero)
                reinicioDelJuego = True
                puntajeActual = calculo_de_puntaje.calculoPuntajeActual(ganaNivel, reinicioDelJuego, lucesRestantes)

                movimientosRestantes = dimensionDelTablero * 3
                tablero = tableroOriginal
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                lucesRestantes = calculoDeLucesRestantes(tablero)
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))

            else:
                tablero = modificadorTablero.modificoTablero(tablero, coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, dimensionDelTablero)
                movimientosRestantes = movimientosRestantes - 1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = calculoDeLucesRestantes(tablero)

                if(lucesRestantes == 0):
                    ganaNivel = True

                elif((lucesRestantes == 0) and (movimientosRestantes == 0)):
                    ganaNivel = False

        if (ganaNivel == True):
            mensajeGanoNivel()
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
            mensajePerdiste()
            menu_de_inicio.mostrarMenuDeInicio()

    if (ganoJuego == True):
        ganaNivel = None
        #tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(ganaNivel, nivel, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
        print("El puntaje total es de: "+ str(tuplaPuntajes[2]))
        tuplaPuntajes = tuplaPuntajes[2]
        for i in tuplaPuntajes:
            contadorNivel = contadorNivel+1
            print("El puntaje obtenido en el nivel "+str(contadorNivel)+" es de "+str(i))
        mensajeGanoJuego()
        menu_de_inicio.mostrarMenuDeInicio()