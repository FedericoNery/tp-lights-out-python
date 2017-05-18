import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios
import calculo_de_puntaje
import sys

def verificoReinicio(numeroDelNivel, modoYDimension):
            tablero = niveles_predeterminados.niveles_predeterminados(numeroDelNivel)
            mostrar_tablero.imprimirTablero(tablero, modoYDimension[1])
            movimientosRestantes = modoYDimension[1] * 3
            return (tablero, movimientosRestantes)

def calculoDeLucesRestantes(tablero):
    cantidadDeLucesRestantes = 0
    estadosDeLucesDelTablero = tablero.values()
    for estadoDeLuz in estadosDeLucesDelTablero:
        if (estadoDeLuz == 'O'):
            cantidadDeLucesRestantes = cantidadDeLucesRestantes + 1
    return (cantidadDeLucesRestantes)

def noSeGanoElJuego(nivelDelJuego,ganoJuego):
    return ((nivelDelJuego<=5) and (ganoJuego))

def muestroEnPantallaLosPuntajes(tuplaPuntajes,gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel):
    tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
    print("El puntaje en el nivel es: " + str(tuplaPuntajes[0]))
    print("El puntaje total es de : " + str(tuplaPuntajes[1]))

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

def principalPredeterminado():
    nivelDelJuego = 1
    reinicioDelJuego = False
    ganoJuego = False
    puntajeActual = 0
    movimientosIniciales = 0
    puntajeTotal_PorNivel = ()
    tableroYMovimientosRestantes = ()
    puntajesPorNivel = [0,0,0,0,0]
    contadorNivel = 0

    while(noSeGanoElJuego(nivelDelJuego,ganoJuego)):

        print("NIVEL " + str(nivelDelJuego)+"\n")
        gananivel = None
        lucesRestantes = 0
        modoYDimension = ("Predeterminado",5)
        tablero = niveles_predeterminados.niveles_predeterminados(nivelDelJuego)
        mostrar_tablero.imprimirTablero(tablero, modoYDimension[1])
        movimientosRestantes = modoYDimension[1]*3
        movimientosIniciales = movimientosRestantes
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
        lucesRestantes = calculoDeLucesRestantes(tablero)

        while(noSeGanoElNivel(movimientosRestantes,gananivel,lucesRestantes)):

            coordenadaIngresadaPorElUsuario = ingreso_de_casilla.validacionIngresoDeCasillero(modoYDimension[1])

            if (coordenadaIngresadaPorElUsuario == "REINICIO"):
                lucesRestantes = calculoDeLucesRestantes(tablero)
                tableroYMovimientosRestantes = verificoReinicio(nivelDelJuego,modoYDimension)
                reinicioDelJuego=True
                tablero = tableroYMovimientosRestantes[0]
                movimientosRestantes = tableroYMovimientosRestantes[1]
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                muestroEnPantallaLosPuntajes(puntajeTotal_PorNivel, gananivel, nivelDelJuego, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
                reinicioDelJuego=False
            else:
                tablero = modificadorTablero.modificoTablero(tablero,coordenadaIngresadaPorElUsuario)
                mostrar_tablero.imprimirTablero(tablero, modoYDimension[1])
                movimientosRestantes = movimientosRestantes-1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = calculoDeLucesRestantes(tablero)

                if(lucesRestantes == 0):
                    gananivel = True
                elif((lucesRestantes > 0) and (movimientosRestantes == 0)):
                    gananivel = False

        if(gananivel):
            mensajeGanoNivel()
            muestroEnPantallaLosPuntajes(puntajeTotal_PorNivel, gananivel, nivelDelJuego, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)

            if(nivelDelJuego == 5):
                ganoJuego = True
            else:
                nivelDelJuego = nivelDelJuego+1

        if(perdioElNivel(movimientosRestantes,gananivel)):
            muestroEnPantallaLosPuntajes(puntajeTotal_PorNivel, gananivel, nivelDelJuego, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
            gananivel = None
            puntajeTotal_PorNivel = calculo_de_puntaje.calculoPuntaje(gananivel, nivelDelJuego, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
            print("")
            print("TABLA DE PUNTAJES FINALES: ")
            print("El puntaje total es de: " + str(puntajeTotal_PorNivel[1]))
            puntajeTotal_PorNivel = puntajeTotal_PorNivel[2]

            for i in puntajeTotal_PorNivel:
                contadorNivel = contadorNivel + 1
                print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))
            mensajePerdiste()
            menu_de_inicio.menu_de_inicio()

    if (ganoJuego):
        gananivel = None
        puntajeTotal_PorNivel = calculo_de_puntaje.calculoPuntaje(gananivel, nivelDelJuego, lucesRestantes, reinicioDelJuego, puntajeActual,puntajesPorNivel)
        print("El puntaje total es de: " + str(puntajeTotal_PorNivel[2]))
        puntajeTotal_PorNivel=puntajeTotal_PorNivel[2]

        for i in puntajeTotal_PorNivel:
            contadorNivel = contadorNivel+1
            print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))
        mensajeGanoJuego()
        menu_de_inicio.menu_de_inicio()

def principalAleatorio(modoYDimension):
    nivel = 1
    reset = False
    ganojuego=False
    movimientosIniciales = 0
    tuplaPuntajes = ()
    puntajeActual = 0
    puntajesPorNivel = [0,0,0,0,0]
    contadorNivel = 0
    tuplaTableroMovimientos = ()
    diccionarioOriginal={}
    while (nivel <= 5):
        gananivel = None
        lucesRestantes = 0
        diccionario_tablero = niveles_aleatorios.generarTableroAleatorio(modoYDimension[1])
        diccionarioOriginal = diccionario_tablero.copy()
        mostrar_tablero.imprimirTablero(diccionario_tablero, modoYDimension[1])
        movimientosRestantes = modoYDimension[1]*3
        movimientosIniciales = movimientosRestantes
        print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
        lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
        while((movimientosRestantes > 0) and (gananivel == None) and (lucesRestantes > 0)):
            Casilla = ingreso_de_casilla.validacionIngresoDeCasillero(modoYDimension[1])
            if (Casilla == "REINICIO"):
                reset=True
                tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual, puntajesPorNivel)
                reset=False
                movimientosRestantes = modoYDimension[1] * 3
                diccionario_tablero = diccionarioOriginal
                mostrar_tablero.imprimirTablero(diccionario_tablero, modoYDimension[1])
                lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
            else:
                diccionario_tablero = modificadorTablero.modificoTablero(diccionario_tablero, Casilla)
                mostrar_tablero.imprimirTablero(diccionario_tablero, modoYDimension[1])
                movimientosRestantes = movimientosRestantes - 1
                print("MOVIMIENTOS RESTANTES: " + str(movimientosRestantes) + "/" + str(movimientosIniciales))
                lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
                if(lucesRestantes == 0):
                    gananivel = True
                elif((lucesRestantes == 0) and (movimientosRestantes == 0)):
                    gananivel = False
        if (gananivel == True):
            mensajeGanoNivel()
            muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            if (nivel == 5):
                ganojuego = True
            else:
                nivel = nivel + 1
        if ((movimientosRestantes == 0) and (gananivel == False)):
            muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            gananivel = None
            tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            print("")
            print("TABLA DE PUNTAJES FINALES: ")
            print("El puntaje total es de: " + str(tuplaPuntajes[1]))
            tuplaPuntajes = tuplaPuntajes[2]
            for i in tuplaPuntajes:
                contadorNivel = contadorNivel + 1
                print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))
            mensajePerdiste()
            menu_de_inicio.menu_de_inicio()

    if (ganojuego==True):
        gananivel=None
        tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
        print("El puntaje total es de: "+ str(tuplaPuntajes[2]))
        tuplaPuntajes=tuplaPuntajes[2]
        for i in tuplaPuntajes:
            contadorNivel=contadorNivel+1
            print("El puntaje obtenido en el nivel "+str(contadorNivel)+" es de "+str(i))
        mensajeGanoJuego()
        menu_de_inicio.menu_de_inicio()