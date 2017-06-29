from nivelesPredeterminados_logger import archivo_log
global dimensionTableroTxt
global nivelDelJuego

def devolverDimensionDelTablero():
    contador = 0
    for linea in archivo_log:
        contador = contador + 1
        if(contador>2):
            #print(linea)
            datoDelArchivo = extraerDatoDelArchivo(linea)
            dimensionTablero = datoDelArchivo[3]
    return dimensionTablero

def extraerDatoDelArchivo(linea):
    nivel = linea[0]
    columna = linea[2]
    fila = linea[4]
    dimension = linea[6]
    estadoDeLuz = linea[8]
    return (nivel,columna,fila,dimension,estadoDeLuz)

def armarDiccionarioConEstadosDeLuces(datoDelArchivo,nivelDelJuego):
    global tablero
    global validacionDimensionTablero
    global dimensionTableroTxt
    nivelDelJuegoTxt = datoDelArchivo[0]
    if(str(nivelDelJuego) == nivelDelJuegoTxt):
        claveTablero = str (datoDelArchivo[1]) + str (datoDelArchivo[2])
        estadoDeLuz = str(datoDelArchivo[4])
        dimensionTableroTxt = str(datoDelArchivo[3])
        tablero[claveTablero] = estadoDeLuz

def generarTablero(nivelDelJuego):
    global tablero
    tablero = {}
    contador = 0
    for linea in archivo_log:
        contador = contador + 1
        if(contador>2):
            #print(linea)
            datoDelArchivo = extraerDatoDelArchivo(linea)
            armarDiccionarioConEstadosDeLuces(datoDelArchivo,nivelDelJuego)
    return tablero


#generarTablero(2)
#print(tablero)
#mostrar_tablero.imprimirTablero(tablero,int(dimensionTableroTxt))
#nivelesPredeterminados_logger.cerrar()


