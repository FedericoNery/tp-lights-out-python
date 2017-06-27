import log

archivo_log = None

def abrir():
    global archivo_log
    archivo_log = log.abrir("errores.txt")

def guardar(texto):
    global archivo_log
    log.guardar(archivo_log,texto)

def cerrar():
    global archivo_log
    log.cerrar(archivo_log)

abrir()

