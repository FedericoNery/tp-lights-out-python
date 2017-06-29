import datetime

def abrir(nombre_log):
    """Abre el archivo de log indicado. Devuelve el archivo abierto.
    Pre: el nombre corresponde a un nombre de archivo válido.
    Post: el archivo ha sido abierto posicionándose al final."""
    archivo_log = open(nombre_log, "r")
    return archivo_log

def guardar(archivo_log, mensaje):
    """Guarda el mensaje en el archivo de log, con la hora actual.
    Pre: el archivo de log ha sido abierto correctamente.
    Post: el mensaje ha sido escrito al final del archivo."""
# Obtiene la hora actual en formato de texto
    hora_actual = str(datetime.datetime.now())
# Guarda la hora actual y el mensaje de error en el archivo
    archivo_log.write("[{}] {}\n".format(hora_actual, mensaje))

def cerrar(archivo_log):
    """ Cierra el archivo de log.
    Pre: el archivo de log ha sido abierto correctamente.
    Post: el archivo de log se ha cerrado. """
    archivo_log.close()