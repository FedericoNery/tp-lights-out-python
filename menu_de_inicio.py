import sys
import mensajes_del_juego
import principal_modo_aleatorio
import principal_modo_predeterminado
import error_logger

def dimensionIngresadaDelTableroValida(numeroDeLaDimensionDelTablero):
    return ((numeroDeLaDimensionDelTablero == '5') or (numeroDeLaDimensionDelTablero == '6')or (numeroDeLaDimensionDelTablero == '7') or (numeroDeLaDimensionDelTablero == '8') or (numeroDeLaDimensionDelTablero == '9')or (numeroDeLaDimensionDelTablero=='10'))

def ingresoDeLaDimensionDelTablero():

    validacionDeLaDimensionElegidaDelTablero = False

    while (not validacionDeLaDimensionElegidaDelTablero):

        numeroDeLaDimensionDelTablero = str(input("Ingrese el numero correspondiente a la dimension del tablero en la que desea jugar "))

        if (dimensionIngresadaDelTableroValida(numeroDeLaDimensionDelTablero)):
            dimensionTablero = int(numeroDeLaDimensionDelTablero)
            print("Se determino jugar al modo aleatorio " + ",la dimension sera de: " + str(dimensionTablero) + " x " + str(dimensionTablero))
            return (dimensionTablero)

        else:
            validacionDeLaDimensionElegidaDelTablero = False
            error_logger.guardarArchivo("Se ingreso mal la dimension del tablero. Valor de Ingreso: " + numeroDeLaDimensionDelTablero)
            print("Error")

def imprimirOpcionesDeJuegoYOpcionSalir():
    print("1.JUGAR MODO ALEATORIO ")
    print("2.JUGAR MODO PREDETERMINADO")
    print("3.SALIR ")

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

def usuarioSeleccionoSalir(numeroDeOpcionElegida):
    return numeroDeOpcionElegida == '3'

def mostrarMenuDeInicio():
    """ Interfaz de inicio del juego para seleccionar entre modo aleatorio o predeterminado. Dentro del modo
    aleatorio se podrá seleccionar la dimension del tablero"""

    mensajes_del_juego.mensaje_de_bienvenida()
    imprimirOpcionesDeJuegoYOpcionSalir()
    validacionDeIngresoDelModoDeJuego = False

    while(not validacionDeIngresoDelModoDeJuego):

        numeroDeOpcionElegida = input("Ingrese el numero correspondiente a la accion que desea realizar ")

        if(usuarioSeleccionoAleatorio(numeroDeOpcionElegida)):
            imprimirDimensionesTablerosAleatorios()
            dimensionTablero = ingresoDeLaDimensionDelTablero()
            principal_modo_aleatorio.principalAleatorio(dimensionTablero)

        elif(usuarioSeleccionoPredeterminado(numeroDeOpcionElegida)):
            print ("Se determino jugar al modo predeterminado \n")
            #dimensionTablero = 5
            principal_modo_predeterminado.principalPredeterminado()
            #principal_modo_predeterminado.principalPredeterminado(dimensionTablero)

        elif(usuarioSeleccionoSalir(numeroDeOpcionElegida)):
            error_logger.cerrar()
            sys.exit()
        else:
            validacionDeIngresoDelModoDeJuego = False
            error_logger.guardar("Se ingreso mal el numero de opcion del menu. Valor de Ingreso: "+ numeroDeOpcionElegida)
            print ("Error")
