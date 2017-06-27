import log

def abrirArchivo():
    log.abrir("errores.txt")

def guardarArchivo(texto):
    log.guardar("errores.txt",texto)

def cerrarArchivo(archivo_log):
    log.cerrar(archivo_log)