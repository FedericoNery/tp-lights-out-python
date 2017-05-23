import sys
import prueba_solo_por_turnos
def mensaje_de_bienvenida():
    print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|")
    print("| B B B    I   E E E  NN    N V       V E E E  NN    N  I  D D D     O O O          A     |")
    print("| B   B    I   E      N N   N  V     V  E      N N   N  I  D     D  O     O        A A    |")
    print("| B B B B  I   E E E  N  N  N   V   v   E E E  N  N  N  I  D     D  O     O       A   A   |")
    print("| B     B  I   E      N   N N    V V    E      N   N N  I  D     D  O     O      A A A A  |")
    print("| B B B B  I   E E E  N    NN     V     E E E  N    NN  I  D D D     O O O      A       A |")
    print("|                                                                                         |")
    print("| L      U     U   C C C  E E E   S S S      F F F  U     U  E E E  R R R       A         |")
    print("| L      U     U  C       E      S           F      U     U  E      R    R     A A        |")
    print("| L      U     U  C       E E E   S S S      F F F  U     U  E E E  R R R     A   A       |")
    print("| L      U     U  C       E            S     F      U     U  E      R   R    A A A A      |")
    print("| L L L   U U U    C C C  E E E   S S S      F       U U U   E E E  R    R  A       A     |")
    print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|\n")

def dimensionIngresadaDelTableroValida(numeroDeLaDimensionDelTablero):
    return ((numeroDeLaDimensionDelTablero == '5') or (numeroDeLaDimensionDelTablero == '6')or (numeroDeLaDimensionDelTablero == '7') or (numeroDeLaDimensionDelTablero == '8') or (numeroDeLaDimensionDelTablero == '9')or (numeroDeLaDimensionDelTablero=='10'))

def ingresoDeOpcionJugarSalir():

    validacionNumeroIngresadoOpcion = False

    while (not validacionNumeroIngresadoOpcion):

        numeroDeOpcionElegida = input("Ingrese el valor numerico de lo que desea hacer ")

        if (numeroDeOpcionElegida == '1'):
            validacionNumeroIngresadoOpcion = True

        elif (numeroDeOpcionElegida == '2'):
            sys.exit()

        else:
            print("Error")

def ingresoDeLaDimensionDelTablero():

    validacionDeLaDimensionElegidaDelTablero = False

    while (not validacionDeLaDimensionElegidaDelTablero):

        numeroDeLaDimensionDelTablero = str(input("Ingrese el numero correspondiente a la dimension del tablero en la que desea jugar "))

        if (dimensionIngresadaDelTableroValida(numeroDeLaDimensionDelTablero)):
            validacionDeLaDimensionElegidaDelTablero = True
            dimensionTablero = int(numeroDeLaDimensionDelTablero)
            print("Se determino jugar al modo aleatorio " + ",la dimension sera de: " + str(dimensionTablero) + " x " + str(dimensionTablero))
            return (dimensionTablero)

        else:
            validacionDeLaDimensionElegidaDelTablero = False
            print("Error")

def imprimirJugarSalir():
    print("1.JUGAR ")
    print("2.SALIR ")

def imprimirAleatorioPredeterminado():
    print("\n")
    print("1.MODO ALEATORIO")
    print("2.MODO PREDETERMINADO\n")

def imprimirDimensionesTablerosAleatorios():
    print("5. Tablero de 5x5")
    print("6. Tablero de 6x6")
    print("7. Tablero de 7x7")
    print("8. Tablero de 8x8")
    print("9. Tablero de 9x9")
    print("10. Tablero de 10x10\n")

def usuarioSeleccionoAleatorio(numeroDeOpcionElegida):
    return numeroDeOpcionElegida == '1'

def usuarioSeleccionoPredeterminado(numeroDeOpcionElegida):
    return numeroDeOpcionElegida == '2'

def mostrarMenuDeInicio():
    """ Interfaz de inicio del juego para seleccionar entre modo aleatorio o predeterminado. Dentro del modo
    aleatorio se podrá seleccionar la dimension del tablero"""

    dimensionTablero = 0
    modoDelJuego = 0

    mensaje_de_bienvenida()
    imprimirJugarSalir()
    ingresoDeOpcionJugarSalir()
    imprimirAleatorioPredeterminado()
    validacionDeIngresoDelModoDeJuego = False

    while(not validacionDeIngresoDelModoDeJuego):

        numeroDeOpcionElegida = input("Ingrese el numero correspondiente a la accion que desea realizar ")

        if(usuarioSeleccionoAleatorio(numeroDeOpcionElegida)):
            validacionDeIngresoDelModoDeJuego = True
            modoDelJuego = "Aleatorio"
            imprimirDimensionesTablerosAleatorios()
            dimensionTablero = ingresoDeLaDimensionDelTablero()

        elif(usuarioSeleccionoPredeterminado(numeroDeOpcionElegida)):
            validacionDeIngresoDelModoDeJuego = True
            print ("Se determino jugar al modo predeterminado \n")
            modoDelJuego = "Predeterminado"
            dimensionTablero = 5

        else:
            validacionDeIngresoDelModoDeJuego = False
            print ("Error")

    ejecutarModoDeJuegoSeleccionado(modoDelJuego,dimensionTablero)

def ejecutarModoDeJuegoSeleccionado(modoDelJuego,dimensionTablero):

    if (modoDelJuego == "Predeterminado"):
        prueba_solo_por_turnos.principalPredeterminado(dimensionTablero)

    elif (modoDelJuego == "Aleatorio"):
        prueba_solo_por_turnos.principalAleatorio(dimensionTablero)
