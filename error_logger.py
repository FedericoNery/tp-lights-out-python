import log

archivo_log_error = None

def abrir():
    global archivo_log_error
    archivo_log_error = log.abrir("errores.txt")

def guardar(texto):
    global archivo_log_error
    log.guardar(archivo_log_error, texto)

def cerrar():
    global archivo_log_error
    log.cerrar(archivo_log_error)

abrir()

