from nivelesPredeterminados_logger import archivo_log

def extraerDatoDelArchivo(linea):
    nivel = linea[0]
    columna = linea[1]
    fila = linea[2]
    dimension = linea[3]
    estadoDeLuz = linea[4]
    return (nivel,columna,fila,dimension,estadoDeLuz)

def armarDiccionarioConEstadosDeLuces(datoDelArchivo):


for linea in archivo_log:
    print(linea)
    extraerDatoDelArchivo(linea)


