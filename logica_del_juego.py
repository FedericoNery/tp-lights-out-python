import niveles_predeterminados

def restablezcoTableroOriginalPredeterminado(nivelDelJuego):
    tablero = niveles_predeterminados.niveles_predeterminados(nivelDelJuego)
    return tablero

def calculoDeLucesRestantes(tablero):
    cantidadDeLucesRestantes = 0
    estadosDeLucesDelTablero = tablero.values()
    for estadoDeLuz in estadosDeLucesDelTablero:
        if (estadoDeLuz == 'O'):
            cantidadDeLucesRestantes = cantidadDeLucesRestantes + 1
    return (cantidadDeLucesRestantes)

def noSeGanoElJuego(nivelDelJuego,ganoJuego):
    return ((nivelDelJuego<=5) and (not ganoJuego))

def noSeGanoElNivel(movimientosRestantes,gananivel,lucesRestantes):
    return ((movimientosRestantes > 0) and (gananivel == None) and (lucesRestantes > 0))

def perdioElNivel(movimientosRestantes,gananivel):
    return ((movimientosRestantes == 0) and (gananivel == False))

def noQuedanLucesPrendidas(lucesRestantes):
    return lucesRestantes == 0

def siQuedanLucesPrendidasYNoQuedanMovimientos(lucesRestantes,movimientosRestantes):
    return ((lucesRestantes > 0) and (movimientosRestantes == 0))

def ganoElJuego(nivelDelJuego,lucesRestantes):
    return nivelDelJuego==5 and lucesRestantes==0


