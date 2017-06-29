import logNivelesPredeterminados

archivo_log = None

def abrir():
    global archivo_log
    archivo_log = logNivelesPredeterminados.abrir("nivelesPredeterminados.txt")

def guardar(texto):
    global archivo_log
    logNivelesPredeterminados.guardar(archivo_log,texto)

def cerrar():
    global archivo_log
    logNivelesPredeterminados.cerrar(archivo_log)

abrir()
