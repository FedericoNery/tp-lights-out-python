global nivelDelJuego
global puntajeActual

def pasarDeNivel(nivelDelJuego):
    return nivelDelJuego+1

def calculoPuntajeActual(puntosObtenidos):
    return puntajeActual+puntosObtenidos

def devuelvoNivelActualDelJuego():
    return nivelDelJuego

def init_Usuario():
    global puntaje,nivel
    puntaje = [0,0,0,0,0]
    nivel = 1