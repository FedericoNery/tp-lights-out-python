import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios
import calculo_de_puntaje
import sys


def verificoReinicio(nivel,modoYDimension,reset,gananivel,lucesRestantes,puntajeActual,puntajesPorNivel):
        reset=True
        if(modoYDimension[0]=="Predeterminado"):
            diccionario_tablero = niveles_predeterminados.niveles_predeterminados(nivel)
            mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
            tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            movimientosRestantes = modoYDimension[1] * 3
            lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
            reset=False
            return (diccionario_tablero)
        elif(modoYDimension[0]=="Aleatorio"):
            diccionario_tablero = niveles_aleatorios.generarTablerosConLuces(modoYDimension[1])
            mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
            movimientosRestantes = modoYDimension[1] * 3
            lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
            reset=False

def calculoDeLucesRestantes(diccionario_tablero):
    listaDeLuces=[]
    lucesRestantes=0
    listaDeLuces = diccionario_tablero.values()
    for i in listaDeLuces:
        if (i == 'O'):
            lucesRestantes = lucesRestantes + 1
            gananivel = False
    return (lucesRestantes)

def muestroEnPantallaLosPuntajes(tuplaPuntajes,gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel):
    tuplaPuntajes = calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
    print("El puntaje en el nivel es: " + str(tuplaPuntajes[0]))
    print("El puntaje total es de : " + str(tuplaPuntajes[1]))

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

def principalPredeterminado():
    nivel=1
    reset=False
    puntajeActual=0
    tuplaPuntajes=()
    puntajesPorNivel=[]
    for i in range (1,7):
        puntajesPorNivel.append(0)
    while(nivel<=5):
        gananivel=None
        lucesRestantes=0
        modoYDimension=("Predeterminado",5)
        diccionario_tablero=niveles_predeterminados.niveles_predeterminados(nivel)
        mostrar_tablero.imprimir_Tablero(diccionario_tablero,modoYDimension[1])
        movimientosRestantes = modoYDimension[1]*3
        lucesRestantes=calculoDeLucesRestantes(diccionario_tablero)
        while((movimientosRestantes>0) and (gananivel==None) and (lucesRestantes>0)):
            Casilla=ingreso_de_casilla.validacionIngresoDeCasillero(modoYDimension[1])
            if (Casilla == "REINICIO"):
                diccionario_tablero=verificoReinicio(nivel,modoYDimension,reset,gananivel,lucesRestantes,puntajeActual,puntajesPorNivel)
            else:
                diccionario_tablero=modificadorTablero.modificoTablero(diccionario_tablero,Casilla)
                mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
                movimientosRestantes=movimientosRestantes-1
                lucesRestantes=calculoDeLucesRestantes(diccionario_tablero)
                muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
                if(lucesRestantes==0):
                    gananivel=True
                elif((lucesRestantes>0) and (movimientosRestantes==0)):
                    gananivel=False
        if(gananivel==True):
            mensajeGanoNivel()
            muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            nivel=nivel+1
        if(movimientosRestantes==0):
            muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            mensajePerdiste()
            sys.exit()

def principalAleatorio():
    nivel = 1
    reset = False
    tuplaPuntajes = ()
    puntajeActual = 0
    puntajesPorNivel = []
    while (nivel <= 5):
        gananivel = None
        lucesRestantes = 0
        modoYDimension = ("Aleatorio", 7)
        diccionario_tablero = niveles_aleatorios.generarTablerosConLuces(modoYDimension[1])
        mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
        movimientosRestantes = modoYDimension[1] * 3
        lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
        while((movimientosRestantes > 0) and (gananivel == None) and (lucesRestantes > 0)):
            Casilla = ingreso_de_casilla.validacionIngresoDeCasillero(modoYDimension[1])

            verificoReinicio(Casilla, nivel, modoYDimension, reset, gananivel, lucesRestantes, puntajeActual,puntajesPorNivel)

            diccionario_tablero = modificadorTablero.modificoTablero(diccionario_tablero, Casilla)
            mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
            movimientosRestantes = movimientosRestantes - 1
            lucesRestantes = calculoDeLucesRestantes(diccionario_tablero)
            muestroEnPantallaLosPuntajes(tuplaPuntajes, gananivel, nivel, lucesRestantes, reset, puntajeActual,puntajesPorNivel)
            if(lucesRestantes == 0):
                gananivel = True
            elif((lucesRestantes == 0) and (movimientosRestantes == 0)):
                gananivel = False
        if (gananivel == True):
            mensajeGanoNivel()
            print(calculo_de_puntaje.calculoPuntaje(gananivel, nivel, lucesRestantes, reset, puntajeActual))
            nivel = nivel + 1
        if (movimientosRestantes == 0):
            print(calculo_de_puntaje.calculoPuntaje(gananivel,nivel,lucesRestantes,reset,puntajeActual))
            mensajePerdiste()
            sys.exit()
#principalPredeterminado()