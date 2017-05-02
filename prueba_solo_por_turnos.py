import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios
import sys

def principal():
    nivel=1
    while(nivel<=5):
        gananivel=False
        lucesRestantes=0
        lucesRestantesNuevas=0
        modoYDimension=("Predeterminado",5)
        diccionario_tablero=niveles_predeterminados.niveles_predeterminados(nivel)
        mostrar_tablero.imprimir_Tablero(diccionario_tablero,modoYDimension[1])
        movimientosRestantes = modoYDimension[1]*3
        listaDeLuces = diccionario_tablero.values()
        for i in listaDeLuces:
            if (i == 'O'):
                lucesRestantes = lucesRestantes + 1
                gananivel = False
        while((movimientosRestantes>=0) and (gananivel==False) and (lucesRestantes>0)):
            Casilla=ingreso_de_casilla.validacionIngresoDeCasillero(modoYDimension[1])
            diccionario_tablero=modificadorTablero.modificoTablero(diccionario_tablero,Casilla)
            mostrar_tablero.imprimir_Tablero(diccionario_tablero, modoYDimension[1])
            movimientosRestantes=movimientosRestantes-1
            listaDeLuces=diccionario_tablero.values()
            for i in listaDeLuces:
                if(i=='O'):
                    lucesRestantesNuevas=lucesRestantesNuevas+1
                    gananivel=False
            lucesRestantes=lucesRestantesNuevas
            lucesRestantesNuevas=0
            if(lucesRestantes==0):
                gananivel=True
        if(gananivel==True):
            print("""
         G G G      A     NN    N   O O O      E E E  L        NN    N  I  V       V  E E E  L
        G          A A    N N   N  O     O     E      L        N N   N  I   V     V   E      L
        G   G G   A   A   N  N  N  O     O     E E E  L        N  N  N  I    V   V    E E E  L
        G     G  A A A A  N   N N  O     O     E      L        N   N N  I     V V     E      L
         G G G  A       A N    NN   O O O      E E E  L L L    N    NN  I      V      E E E  L L L
        """)
            nivel=nivel+1
        if(movimientosRestantes==0):
            print("""
        P P P   E E E  R R R    D D D   I   S S S  T T T  E E E
        P    P  E      R    R   D    D  I  S         T    E
        P P P   E E E  R R R    D    D  I    S S     T    E E E
        P       E      R    R   D    D  I       S    T    E
        P       E E E  R     R  D D D   I  S S S     T    E E E
        """)
            sys.exit()
principal()